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
date: 2025-03-10
type: meeting-notes
tags: [freshtech, bot, contract, budget]
---

# [[Freshtech Bot Project]]

## Summary
Freshtech initially requested a hotel bot with a contract starting March 10, a $15k budget, and a 3‑month duration. A follow‑up email indicated a shift to a clinic bot, with an end‑of‑April timeline, a $25k budget, and pending CTO confirmation.

## Key Details
- Initial request (meeting notes): hotel bot, contract start **March 10**, budget **$15k**, 3‑month deal, contact **Priya**
- Follow‑up email to Priya: clinic bot instead, timeline **end of April**, budget **$25k**, awaiting CTO confirmation
- Contact person: **Priya** (Freshtech)

## Action Items
- (No explicit action items stated in the notes)

## Notes on Data Quality
<!-- If there are contradictions, missing info, or mixed topics, note them here. Otherwise leave brief. -->
Contradiction: initial notes specify a **hotel bot** while the follow‑up email states a **clinic bot**. Also conflicting timelines (March 10 start vs end‑of‑April) and budgets ($15k vs $25k). The exact date of the meeting/email is not provided; the contract start date (March 10) is used as a placeholder for the date field.

## Related
- [[Freshtech]]
- [[Hotel Bot]]
- [[Clinic Bot]]
