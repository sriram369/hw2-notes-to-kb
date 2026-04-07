# case_4_hard_contradiction
**Category:** hard_fail
**Description:** Conflicting client meeting notes
**Prompt version:** v2

## Raw Input
```
client meeting notes — freshtech: they want a hotel bot for sure. contract starts next monday march 10. budget is 15k, 3-month deal. contact person is priya.
---
follow-up email to priya at freshtech: she said they want a clinic bot instead. timeline is end of april. budget now 25k. waiting on their CTO to confirm.
```

## Expected Behavior
Should FLAG the contradiction (hotel vs clinic, 15k vs 25k, march vs april) and NOT silently pick one side. Should recommend human review.

## LLM Output
# Freshtech Bot Project
## Summary
Freshtech initially requested a hotel bot with a contract starting March 10, a 15k budget for a 3‑month deal, and Priya as the contact. After a follow‑up email, Priya indicated they now prefer a clinic bot, increased the budget to 25k, set the timeline for end of April, and are awaiting CTO confirmation.
## Key Details
- Initial request: hotel bot
- Contract start: Monday, March 10
- Initial budget: 15k, 3‑month deal
- Contact person: Priya
- Updated request: clinic bot
- Updated budget: 25k
- Timeline: end of April
- Awaiting CTO confirmation
## Action Items
- [ ] Prepare revised proposal for clinic bot (who: you, deadline: 2025-03-17)
- [ ] Follow up with Priya for CTO confirmation (who: you, deadline: 2025-04-15)
## Tags
#Freshtech #BotProject #ClinicBot #HotelBot
