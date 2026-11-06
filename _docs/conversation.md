---
title: Conversations and Follow-ups
layout: post
category: docs
permalink: /docs/conversation/
date: 2026-07-07
---

# Conversations and follow-ups

People rarely ask one self-contained question. They ask about a room, then say "and the humidity
there?", "plot that", "the second one" or "how do you know that?". This page explains how OntoSage
remembers a conversation, how it turns a follow-up into a question it can answer, when it asks
instead of guessing, and how a fault reported in chat becomes a tracked report. It is for developers
working on memory or routing, and for users who want to know what OntoSage will and will not carry
from one turn to the next.

Paths are relative to `orchestrator/` unless they start with `shared/`. The full request path is in
[How OntoSage Answers a Question]({{ '/docs/how-it-answers/' | relative_url }}).

## Where a conversation is kept

| Store | What it holds | Bounded by |
|---|---|---|
| Redis `conversation:<id>` | The working copy of the conversation state: messages and the state bus (`intermediate_results`) | `CONVERSATION_MAX_MESSAGES` (default 400 messages). No time expiry while `CONVERSATION_TTL=0` (the default). |
| Postgres `messages` | The full transcript, kept until the user deletes the conversation | Not pruned |
| Postgres `turn_memory` | One row per completed turn: the user's question, intent, entities, a one-line summary, carried-forward results and a bounded projection of the evidence record (`services/turn_memory.py`) | The newest 500 turns per conversation |
| Qdrant `user_memory` | Cross-session memories for a signed-in user (`services/agent_memory.py`) | `CROSS_SESSION_MEMORY_ENABLED` (default `true`); never used for the shared anonymous identity |

Trimming the Redis copy loses nothing: `_fill_history_gap` in `main.py` refills it from Postgres on
every chat route when the stored transcript is longer. Open WebUI also keeps its own copy of each chat
for display; OntoSage does not depend on it.

**What each model call sees.** No prompt receives the whole history. Intent classification sees the
last five messages and a short running summary; the follow-up rewrite sees the last six messages.
Older turns reach the model only through the **session summary**.

### The session summary

Before every turn, `_inject_session_summary` (`main.py`) builds a summary of older turns with
`services/session_summary.py` and puts it in `intermediate_results["session_summary"]`. It is built
under two rules:

- **No figures from past answers.** A past turn contributes its subject and a one-word outcome, never
  its answer text. A number remembered from twenty turns ago, restated as if current, would be a
  fabrication that nothing could contradict.
- **The user's own questions are kept**, with anything that looks like a measurement redacted. Room
  and floor identifiers survive; "1,200 ppm" does not.

The three most recent turns are left out because the raw messages already cover them; the next ten
appear as short lines; anything older is compressed into one line naming the subjects in the order
they first appeared. The block is capped at 2,200 characters. The same rows, kept structured, are what
the [session recall](#what-did-i-ask-earlier) lane reads.

## Carry-forward: "now plot that"

Some results are worth keeping for the next turn. `TurnMemoryService` saves three keys with each turn
in Postgres, and `/v1/chat/completions` restores them on the next (`get_carry_forward`, falling back to
the Redis copy). The other chat routes restore the whole state bus from Redis, which includes them.

- `forecast_result` and `analytics_result`, so "plot that" or "graph it" draws the result the user just
  saw. The visualization node plots a stored forecast directly instead of asking the model to write
  chart code from nothing.
- `remembered_location`, set whenever a message says where the user is ("I am in room ..."). It lasts
  for the session, and nearest-facility answers measure from it, saying so in their first line.

If the previous answer offered a chart and the user replies "yes please" or "go ahead",
`_affirmation_to_chart` turns the reply into the chart request the earlier question implied.

**A carried result belongs to a place.** `_prune_inherited_state` (with
`context_switch.prune_inherited`) drops carried, place-bound results when the new question names a
different place from the last one named. "What about room 3.01? Plot it" will not draw a chart of the
previous room's data under the new room's name. A follow-up that names no place keeps them.

## Turning a follow-up into a question

Every later stage (classification, entity extraction, the existence check, SPARQL) reads one string:
the latest message. So a follow-up is rewritten into a self-contained question first, in
`DialogueAgent.rewrite_to_standalone` (`agents/dialogue_agent.py`). The step is controlled by
`COREFERENCE_REWRITE_ENABLED` (default `true`). The original wording is kept in the message metadata
and in `intermediate_results["coref_rewrite"]`.

![A follow-up resolved from the previous turn]({{ '/assets/images/screenshots/chat-follow-up.png' | relative_url }})
*A follow-up resolved from the previous turn: the second question names no place, and the answer is
about the place the conversation was already discussing.*

The steps, in order:

1. **Provenance questions are left alone.** "How do you know that?" refers to the previous answer, not
   to an entity, so it is not rewritten (see [below](#how-do-you-know-that)).
2. **Deterministic resolvers run first.** They copy words from the conversation into the question
   without calling a model. The first one that applies wins.
3. **Ambiguity is asked about.** If the previous reply named several rooms and the follow-up asks a
   value of "there" or "it", OntoSage asks which one.
4. **The model rewrite runs last**, only for a message that looks like a follow-up (short, or starting
   with "and", "what about", or carrying "there", "that", "the same"). It sees the last six messages and
   the session summary, and is told to keep time words as written.
5. **The rewrite is checked.** It is rejected if it changes a place the user named
   (`context_switch.rewrite_is_safe`), or binds a place no user message ever named
   (`rewrite_invents_a_place`), unless it is the place the previous reply named for this very word
   (`previous_reply_named_it`). Any year that no message contains is removed
   (`strip_invented_years`). A rejected rewrite leaves the original message in place.

### The deterministic resolvers

All live in `services/context_switch.py`. Each takes the latest message and one piece of context, and
returns a rewritten question or nothing.

| Resolver | Follow-up shape | Resolved from |
|---|---|---|
| `resolve_report_reference` | "what is the status of that report?" | The report id the previous reply filed |
| `resolve_ordinal` | "the first one", "the second one" | The list in the previous reply |
| `resolve_sole_record_anaphor` | "when is it due?" | The one record (a work order, say) the previous reply named |
| `resolve_sole_room_anaphor` | "is it free this afternoon?", "and the CO2 there?" | The one room the previous reply named |
| `resolve_location_statement` | "I am in room ..." straight after a nearest-facility question | The previous question, asked again from that room |
| `resolve_relative_day_followup` | "and the day before?" | The previous question, its day moved back one |
| `resolve_counted_instruments` | "what did they record?" after a count of instruments | The previous question's instruments |
| `resolve_elliptical_superlative` | "which floor used the most?" | The quantity and period of the user's earlier question |
| `resolve_compare_with_before` | "how does that compare with the week before?" | The user's earlier question and its period |
| `resolve_place_swap` | "what about room ...?" | The previous question with only its place changed |
| `resolve_pair_reference` | "which of the two is busier?" | Exactly two places the user named in earlier turns |
| `resolve_sole_floor_or_amenity_anaphor` | "what time does it close?" | The one amenity or floor the previous reply named, matched against the building's own amenity terms |

Resolvers that look at "the user's earlier question" read the **user's** words, never the assistant's,
because a model's earlier rewrite may already have been wrong. `resolve_pair_reference` needs exactly
two places; with more or fewer, OntoSage asks which two.

## When OntoSage asks instead of guessing

A clarification question costs the user one reply. Answering about the wrong room costs them an
answer that looks right. OntoSage asks in these cases:

| Situation | Where | What is asked |
|---|---|---|
| A follow-up says "there" or "it" and the previous reply named several rooms | `context_switch.ambiguous_reference`, then `detect_intent` | Which of the listed rooms is meant |
| The question says "this room" or "here" and no room has been named in the conversation | `referent_resolver.detect_space_deixis` and `ask_which_space` | Which room, by number or name, or which floor to narrow it down |
| A room id matches several real rooms and names none exactly | `ReferentResolver.resolve` (`ambiguous`) | Which of the matching rooms |
| A sensor reference is ambiguous | `DisambiguationService.check_and_clarify_with_context` (`services/disambiguation_service.py`) | Which sensor or zone; the reply is read on the next turn by `extract_clarification_answer` |
| A deliberation question has an unclear constraint | `services/deliberation/clarify_policy.py` | One question; the reply resumes the parked plan |
| A request is too vague ("fix everything"), or a plan depends on the asker's own commitments | routing rules `vague_complaint_clarify`, `plan_around_my_own_commitments` | What is meant |
| A message refers to an earlier reply in a conversation that has none | `_dialogue_node` | Nothing is accepted on a false premise; the reply says this is the first message and asks what is meant |

**Endpoint difference.** On `/chat`, `/chat/stream` and the websocket, the whole state bus is restored
from Redis each turn, so a parked clarification (an ambiguous sensor, a deliberation constraint) is
picked up directly from the bus. On `/v1/chat/completions`, which Open WebUI uses, the bus is rebuilt
each turn and only the carry-forward keys survive; the reply to a clarification is understood through
the conversation history and the follow-up rewrite.

## "What did I ask earlier?"

Questions about the conversation itself ("what have we discussed so far?", "which floor did I mention
before?") are recognised by `session_recall.is_recall_question` and routed by the `session_recall`
rule to the `session_recall` lane. The classifier is never asked to pick this lane, because such
questions often contain room and record words and would otherwise look like data questions.

The lane **quotes**: it reads back the user's own earlier questions with their turn numbers, oldest
first, filtered to the subject asked about. It never interprets what the user "meant", so it cannot
name a room the user did not type. It recalls subjects, not values, and every answer ends with that
caveat:

> I can recall what was **asked**, not what was answered: this session record keeps no measured values
> on purpose, so nothing above is a reading. Ask again for any figure and I will re-query the data.

## "How do you know that?"

A question about the previous answer ("how do you know that?", "where did that number come from?",
"what sources did you use?") matches `answer_provenance.PROVENANCE_RE`. The routing rule
`answer_provenance` sends it to the capability lane, which loads the **previous** turn's evidence
record from the conversation's saved state in Redis and reads it back with `answer_provenance.render`.
(The session-recall lane uses the same read, `load_previous_turn_record`, for "what is the evidence
behind your last answer?".) That is the same renderer that builds the *How I know this* panel under an
answer, so the two always agree. The read-back says whether the answer was replayed from cache, and
ends by noting that it is the answer's own record, kept at the time, not a reconstruction.

If the previous turn has no evidence record, the reply says so and explains that it will not
reconstruct an explanation after the fact.

## Reporting a fault from chat

A statement that something is wrong is filed, not answered. The routing contract separates the two:
`report_intake_statement` sends a fault, complaint or safety **statement** to report intake, while
`question_is_not_a_report` and the checks inside `_report_intake_node` make sure a **question** ("is
the lift broken?") is answered and never filed.

1. **File.** `services/report_intake_service.py` writes a row to the Postgres `user_reports` table:
   category (maintenance, complaint, safety, feedback, suggestion), priority (safety and urgency words
   raise it), location and device if the message names them, the reporter and the conversation.
2. **Acknowledge.** The reply gives a tracking id (`REP-` followed by six characters), the category,
   priority and status, and tells the user how to check progress.
3. **Ask where, once.** If a maintenance, safety or complaint report names no room, floor or
   equipment, the reply asks which. It asks at most once, so a bare reply cannot start a loop.
4. **Urgent reports** also tell the user to call the building's emergency line for a fire, gas, flood
   or injury.
5. **Follow up.** "What is the status of REP-..." looks the report up, limited to the asker's own
   reports. "What is the status of that report?" works too: `resolve_report_reference` puts the id from
   the previous reply into the question. A message asking for "my reports" lists them.

Examples from the intent file: *"the light in room 3.01 is broken"*, *"the fire exit on floor 3 is
blocked by boxes"*, *"what is the status of REP-A1B2C3"*.

## Settings that affect conversations

| Setting | Default | Effect |
|---|---|---|
| `CONVERSATION_MAX_MESSAGES` | 400 | Messages kept in the Redis working copy |
| `CONVERSATION_TTL` | 0 | Seconds before Redis expires a conversation; 0 means never |
| `MAX_CONVERSATION_HISTORY` | 400 | Prior messages carried per turn from the client or the store |
| `COREFERENCE_REWRITE_ENABLED` | `true` | The model rewrite of follow-ups (the deterministic resolvers sit in the same function) |
| `CROSS_SESSION_MEMORY_ENABLED` | `true` | Memories from a signed-in user's earlier sessions in the classification prompt |
| `TRUST_FORWARDED_USER` | `false` | Use the Open WebUI user's identity; without it, Open WebUI chats share one least-privileged identity and get no cross-session memory |

See [Configuration]({{ '/docs/configuration/' | relative_url }}) for the full list.
