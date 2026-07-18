---
title: Stakeholder Guide
layout: post
category: docs
permalink: /docs/stakeholder-guide/
date: 2026-07-07
---

# Stakeholder guide — what can I ask?

OntoSage answers one interface for everyone in and around the building. You don't need SQL, SPARQL, or
any schema knowledge — you ask in plain English. This page shows the kinds of questions each stakeholder
tends to bring, and what data each needs behind the scenes.

Personas here **frame** the answer (wording, emphasis) — they do **not** decide what you're allowed to
see. Access is controlled separately by [RBAC]({{ '/docs/security-rbac/' | relative_url }}).

You ask in plain English and get an answer plus its provenance and how it routed — here in the admin
console's Ask tab, or through the chat UI:

![Ask tab showing a grounded, sourced answer]({{ '/admin-portal-screenshots/03b-ask-answer.png' | relative_url }})
*A plain-English question — "How many rooms are there?" — answered with real figures computed live from
the ontology and floor plans, every block cited to its source, with the routed intent shown. If a
referent doesn't exist, OntoSage says so rather than inventing a number.*

## Everyone — plain-English, grounded

- *"Is it stuffy on floor 5?"* → resolves "stuffy" to CO₂ sensors, reads them live, answers in plain
  terms.
- *"Where's the nearest prayer room / cafe / accessible toilet?"* → the [OCBV]({{ '/docs/ocbv-schema/' | relative_url }})
  capability layer.
- *"The toilet on floor 2 is leaking — who do I tell?"* → recognised as a **fault report**, filed, and
  answered with who to contact (not mistaken for a data question).
- *"Show me floor 3."* → the floor-plan manifest renders the map.

If a sensor isn't modelled or its readings aren't loaded, OntoSage **says so** rather than inventing a
number.

## By stakeholder

| Stakeholder | Typical questions | What it needs |
|---|---|---|
| **Occupant / visitor / student** | "Is it too warm in here?", "Where can I get coffee?", "How do I book a lab?" | CO₂/temp sensors; OCBV amenities; procedure knowledge topics |
| **Facility manager** | "Which zones are over 26 °C right now?", "Any anomalies today?", "Show open fault reports" | Live time-series + analytics; report intake |
| **Sustainability officer** | "What's energy use this week vs last?", "Trend the CO₂ on floor 4" | Time-series + analytics + forecasting |
| **Safety officer** | "Any smoke/CO alerts?", "Log a safety hazard on floor 1" | Alert sensors; safety-report intake |
| **Researcher** | "List all Brick Temperature_Sensor instances", "Give me the SPARQL for zone occupancy" | The raw ontology + SPARQL browser |
| **Executive / admin** | "How many sensors are online?", "Summarise building health" | Aggregate SPARQL + health |

## The question types it routes between

OntoSage classifies each question into an intent and routes it to the right agent:

- **Locate / Discover** — where things are, what exists (floor plan, spatial, SPARQL).
- **Quantify** — counts and current values ("how many…", "what is… right now").
- **Trend / Forecast** — change over time, projections.
- **Compare** — floor vs floor, week vs week.
- **Anomaly** — what's out of range.
- **Comfort** — subjective questions ("is it stuffy/warm?") mapped to the right sensor.
- **Procedure** — how-to and policy from the capability/document KB.
- **Report** — statements of a fault/complaint/hazard/suggestion, filed for action.

A question that mixes two ("show me floor 3 **and** how many rooms are there") is decomposed and each
part routed independently, then the answers are fused.

## What it will *not* do

- **Actuate.** "Open the windows", "set the thermostat to 21", "email facilities" are politely declined
  — OntoSage answers, it doesn't operate the building.
- **Invent.** No data → an honest "no data", never a plausible guess.
- **Cross buildings.** One active building per deployment.

## See also

- [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) — the amenity/procedure/report layer behind the non-sensor answers.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}) — personas vs. permissions.
- [Architecture]({{ '/docs/architecture/' | relative_url }}) — how a question is routed.
