# case_4_hard_contradiction
**Category:** hard_fail
**Description:** Conflicting client meeting notes
**Prompt version:** v3

## Raw Input
```
client meeting notes — freshtech: they want a hotel bot for sure. contract starts next monday march 10. budget is 15k, 3-month deal. contact person is priya.
---
follow-up email to priya at freshtech: she said they want a clinic bot instead. timeline is end of april. budget now 25k. waiting on their CTO to confirm.
```

## Expected Behavior
Should FLAG the contradiction (hotel vs clinic, 15k vs 25k, march vs april) and NOT silently pick one side. Should recommend human review.

## LLM Output
---
title: Freshtech Client Engagement
date: YYYY-MM-DD
type: meeting-notes
tags: [client, freshtech, bot-development, sales]
---

# [[Freshtech Client Engagement]]

## Summary
Initial discussions with [[Freshtech]] regarding a custom bot project have shifted significantly between the initial meeting and a subsequent follow-up email. The project scope, budget, timeline, and deliverables are currently in flux pending confirmation from their CTO.

## Key Details
- Client: [[Freshtech]]
- Primary Contact: [[Priya]]
- Initial Meeting Details:
  - Requested deliverable: Hotel bot
  - Contract start date: next monday march 10
  - Budget: 15k
  - Contract term: 3-month deal
- Follow-up Email Details:
  - Requested deliverable: Clinic bot
  - Timeline: end of april
  - Budget: 25k
  - Status: Waiting on their CTO to confirm

## Action Items
- [ ] Await confirmation from [[Freshtech]] CTO regarding clinic bot scope and updated budget (status: pending per notes)

## Notes on Data Quality
- **Explicit Conflict:** The notes contain direct contradictions between the initial meeting and the follow-up email. The deliverable changed from a "hotel bot" to a "clinic bot". The start date shifted from "next monday march 10" to "end of april". The budget increased from "15k" to "25k". The "3-month deal" term is only mentioned in the initial notes and is absent from the follow-up.
- **Missing Information:** Exact dates for the meeting and follow-up email are not provided. The CTO's name is unspecified. Clarification is required to determine which set of terms is currently active.

## Related
- [[Freshtech]]
- [[Hotel Bot]]
- [[Clinic Bot]]
- [[Sales Pipeline]]
