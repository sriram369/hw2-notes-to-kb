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
title: Freshtech Meeting – Hotel Bot Contract Details
date: 2025-09-26
type: meeting-notes
tags: [freshtech, hotel bot, contract, march 10, budget 15k, 3-month deal, priya, clinic bot, april, budget 25k, CTO]

# [[Freshtech Meeting – Hotel Bot Contract Details]]

## Summary
The client meeting notes from freshtech indicate they want a hotel bot, with contract starting next Monday March 10, budget 15k for a 3-month deal, contact person Priya; a follow-up email to Priya states they want a clinic bot instead, timeline end of April, budget now 25k, and they are waiting on their CTO to confirm.

## Key Details
- Hotel bot requested.
- Contract start: Monday, March 10.
- Budget: 15k, 3-month deal.
- Contact person: Priya.
- Follow-up email: Priya wants clinic bot instead.
- Timeline: end of April.
- Updated budget: 25k.
- Waiting on CTO confirmation.

## Action Items
- [ ] Confirm contract start date with legal team.
- [ ] Arrange budget allocation for 3-month deal.
- [ ] Coordinate with Priya for hotel bot requirements.
- [ ] Schedule follow-up for clinic bot specifications.
- [ ] Prepare timeline for end of April deliverables.
- [ ] Verify CTO availability and confirmation.

## Notes on Data Quality
- No explicit meeting date provided; assumed placeholder used.
- Some details (e.g., exact budget figures) may need verification.
- Potential conflict between hotel bot and clinic bot requirements needs clarification.

## Related
- [[Hotel Bot Project]]
- [[Clinic Bot Initiative]]
- [[Freshtech Vendor Management]]
