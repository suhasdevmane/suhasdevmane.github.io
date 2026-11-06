---
title: Stakeholder Guide
layout: post
category: docs
permalink: /docs/stakeholder-guide/
date: 2026-07-03
---

# Stakeholder guide: what can I ask?

One chat interface serves everyone who uses or runs the building. You ask in plain English; you do
not need sensor names, ids, SQL or SPARQL. This page shows the kinds of questions people bring,
with examples taken from the repository's own question banks
(`orchestrator/intents/intent_definitions.yaml`, `README.md`, `docs/USER_GUIDE.md` and
`docs/DEMO_QUESTION_BANK.md`), and what the building needs for each to be answerable.

Two rules apply throughout:

- **An answer is only as good as the building's data.** A reading needs the sensor in the graph
  and its rows in a database; an amenity needs its triple; a policy needs its topic or document.
  When something is missing, OntoSage says so rather than substituting something else.
- **Personas frame, roles decide.** A persona (student, researcher, facility manager, occupant,
  energy manager, safety officer, IT administrator, executive, sustainability officer, general)
  changes emphasis and wording. What you may see is set by your account's role; see
  [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}).

## How to ask

- **Name the place and the time** when they matter: "floor 3", "room 5.01", "last week",
  "since this morning". Without a time, a reading question means "now".
- **Follow up naturally.** After *"What is the CO₂ level in Zone 5?"*, a question such as
  *"What about yesterday?"* or *"And what about humidity there?"* is rewritten into a complete
  question before it is answered. After a forecast or an analysis, *"now plot that"* reuses the
  previous result. See [Conversation]({{ '/docs/conversation/' | relative_url }}).
- **Ask for the form you want.** "Plot", "export as CSV" and "show me floor 3" produce a chart, a
  file or a floor plan.
- **Expect a clarifying question** when a name matches several places. Answer it and the
  original question continues.
- **Ask what it can do.** *"What kind of questions can I ask you?"* lists the capability groups of
  the active building.

## Kinds of question

| Kind | Examples | What the building needs |
|---|---|---|
| Current readings | *What is the current temperature in zone 5.28?* · *What is the CO₂ level in Zone 5 right now?* | Sensors in the graph, readings in a database |
| History, trends and forecasts | *How has CO2 changed since Monday?* · *Is energy consumption trending up?* · *Forecast energy usage for next week.* | Enough history for the period asked about |
| Statistics | *What is the average CO2 last week?* · *How many hours was Zone 2 above 25°C this week?* | Readings over the period |
| Comparisons | *Compare air quality between floor 1 and floor 5.* · *How does this week compare to last week?* | Sensors on both sides |
| Charts and exports | *Plot temperature in zone 5.28 over the last 24h.* · *Export last week's data as CSV.* | Readings; links point at `STATIC_BASE_URL` |
| Unusual readings and causes | *Any unusual readings today?* · *Why is it so stuffy in RM125?* | Readings, and records of what changed |
| Choosing a space | *Where can I sit tomorrow that is quiet, with good air, near drinking water?* · *Rank the meeting rooms by CO2.* | Several quantities per space; capacity and booking records for criteria such as seats or availability |
| What exists | *What sensors are in zone 5?* · *How many sensors does the building have?* · *What can you measure in room 2.14?* | The graph only |
| Floor plans and space | *Show me floor 3 plan.* · *Which rooms are adjacent to 3.01?* · *What is the total area of floor 3?* | PDF or DWG per floor; DWG for areas and adjacency |
| Amenities, policies, procedures | *Where is the prayer room?* · *What are the fire evacuation procedures?* · *What happens during a power outage?* | Amenity and knowledge-topic triples; documents a topic names |
| Records and registers | *Which compliance checks are overdue?* · *When was the fire alarm last tested?* · *How many open work orders are there?* · *Is RM101 free at 3pm today?* | The register loaded as records |
| Status of equipment and services | *Are the lifts working?* · *Is the wifi down on floor 3?* · *When was floor 2 last cleaned?* | Asset state and service records |
| Room readiness and comfort history | *Is room 1.06 ready for my class?* · *When was room 2.01 last comfortable?* | Readings, timetable and booking records, comfort bands |
| Compliance with standards | *Is CO2 within safe limits?* · *Is zone 5 within ASHRAE 55 limits?* | Readings and the standards bands the building uses |
| Reporting a problem | *The light in room 3.01 is broken.* · *There is a trip hazard near the lifts.* · *Suggestion: please add more bike racks outside.* | Nothing: the report is stored with a tracking id |
| Personal alerts and preferences | *Alert me if CO2 exceeds 1000 ppm in any zone.* · *Remember that I prefer temperatures between 22 and 24 degrees.* | A signed-in account |
| The conversation itself | *What did I ask about earlier?* · *Which floor did I mention before?* | The current conversation |
| OntoSage itself | *What is OntoSage?* · *What can you do?* · *How do you work?* | Nothing: answered from configuration |

![A chart produced from readings]({{ '/assets/images/screenshots/chat-chart.png' | relative_url }})
*Asking for a plot returns a chart built from the readings the answer used.*

![A floor plan shown in the chat]({{ '/assets/images/screenshots/chat-floor-plan.png' | relative_url }})
*A floor plan request shows the plan in the conversation.*

![An answer from a building document]({{ '/assets/images/screenshots/chat-document.png' | relative_url }})
*A policy question answered from the document the building's graph names for it.*

## By stakeholder

| Stakeholder | Questions they tend to ask |
|---|---|
| **Occupants, students, visitors** | *Is it too warm in here?* · *Where is the prayer room?* · *Is the building pushchair-friendly from the car park?* · *I'm pregnant and overheating - where's the coolest place to work today?* · *Is tap water free somewhere, or do I have to buy bottles?* |
| **Lecturers and room users** | *Is room 1.06 ready for my class?* · *Find a room for 12 with a projector, free 2-4pm today, near the cafe.* · *What should I know before teaching in 3.13?* |
| **Facility managers and operators** | *Which plant items are running outside their normal schedule right now?* · *How many open work orders are there, and which are overdue?* · *What maintenance work is scheduled this week?* · *What's the delta-T across the heating circuit, and is it healthy?* |
| **Energy and sustainability staff** | *What is the energy consumption today?* · *Compare floor 3 vs floor 4 energy.* · *Forecast energy usage for next week.* · *Suggest energy saving measures.* |
| **Health, safety and fire staff** | *When was the fire alarm last tested?* · *Which compliance checks are overdue?* · *Is CO2 within safe limits?* · *The fire exit on floor 3 is blocked by boxes.* |
| **Maintenance contractors** | *What's the filter size for the FCUs on floor 4?* · *Where can I isolate the water supply for the second-floor toilets?* |
| **Researchers and data scientists** | *What sensors are available in the building?* · *What type of sensor is X?* · *Export the last 30 days of temperature data for all zones as CSV.* · *Can you measure formaldehyde in room 5.01?* |
| **Executives** | *Give me a daily building performance report.* · *Summarise the air quality conditions across all zones for this week.* |
| **Administrators** | Everything above, plus the [admin console]({{ '/docs/admin-console/' | relative_url }}) and the SPARQL browser. When a question cannot be answered, an administrator is also told what to add. |

Some of these examples ask for information a given building may not record (filter sizes, isolation
points, water provision). For those, a correct answer can be a statement that the building's
records do not hold it.

## What it will not do

| Request | What happens |
|---|---|
| *Turn off the lights in room 2.04* · *Set HVAC zone 3 to 21°C* | The control lane refuses roles without `control:write`. With it, the command is queued in a simulated actuation gateway; no live system is operated by default. |
| *Book me a hotel near the building for tomorrow.* | Declined as outside the building. |
| *Is the professor in her office right now?* | Refused: OntoSage does not locate named people. |
| *Show me the swimming pool temperature* · *Plot the methane concentration* | The building has no such space or sensor; the answer says so and does not substitute another reading. |
| *Should I buy Bitcoin?* | Outside what the building's data can ground: a short statement of what OntoSage can answer from, not a guess. |
| *How do I control CO2?* · *What does a delta-T mean?* | General building knowledge that needs no data from this building is answered as general guidance, labelled as not coming from the building's records. |

Why a question is declined, and how declines are worded, is covered in
[Checks and honest answers]({{ '/docs/checks-and-honesty/' | relative_url }}).

![An honest decline]({{ '/assets/images/screenshots/chat-decline.png' | relative_url }})
*The building does not hold what was asked for, and the answer says so.*

## See also

- [Answer lanes]({{ '/docs/answer-lanes/' | relative_url }}): how each kind of question is answered.
- [Conversation]({{ '/docs/conversation/' | relative_url }}): follow-ups, memory and context.
- [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}): the amenity, policy and record layer behind non-sensor answers.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}): roles and personas.
