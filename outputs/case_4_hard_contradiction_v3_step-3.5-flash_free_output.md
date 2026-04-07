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
None
