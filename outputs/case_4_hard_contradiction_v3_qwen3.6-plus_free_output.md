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
title: Freshtech Bot Project
date: YYYY-MM-DD
type: meeting-notes
tags: [client-meeting, scope-change, freshtech, bot-development]
---

# [[Freshtech Bot Project]]

## Summary
Initial discussions with [[Freshtech]] outlined a hotel bot project with a March 10 start date and a 15k budget. A subsequent follow-up with contact [[Priya]] indicates a complete shift to a clinic bot, a revised timeline of end of April, and an increased budget of 25k, pending final approval from their CTO.

## Key Details
- Client: [[Freshtech]]
- Primary Contact: [[Priya]]
- **Initial Scope:** Hotel bot
- **Updated Scope:** Clinic bot (per follow-up email)
- **Initial Contract Start:** Next Monday, March 10
- **Updated Timeline:** End of April
- **Initial Budget:** 15k (3-month deal)
- **Updated Budget:** 25k
- **Current Status:** Waiting on [[Freshtech]] CTO to confirm updated scope and terms

## Action Items
- [ ] Await confirmation from [[Freshtech]] CTO regarding clinic bot scope, 25k budget, and end of April timeline (assigned to: [[Priya]] / [[Freshtech CTO]], deadline: end of April)

## Notes on Data Quality
- **Explicit Conflict/Scope Change:** The notes contain directly conflicting information between the initial meeting and the follow-up email regarding project type (hotel bot vs. clinic bot), timeline (March 10 vs. end of April), and budget (15k vs. 25k). This appears to be a documented scope evolution, but the exact terms of the final agreement are unconfirmed.
- **Missing Information:** The specific year for "March 10" is not stated. The exact dates of the initial meeting and the follow-up email are missing. The note date is unspecified.

## Related
- [[Freshtech]]
- [[Bot Development]]
