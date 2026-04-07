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
title: Freshtech Bot Project Requirements
date: 2025-03-10
type: meeting-notes
tags: [freshtech, bot, hotel, clinic, budget, timeline]
---

# [[Freshtech]] Bot Project Requirements

## Summary
Freshtech initially requested a hotel bot with a contract start on March 10, a $15k budget for a 3‑month deal. Later they changed the request to a clinic bot, moved the timeline to end of April, increased the budget to $2 
