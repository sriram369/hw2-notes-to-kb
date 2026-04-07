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
title: Freshtech Client Meeting - Bot Project
date: 2025-03-07
type: meeting-notes
tags: [freshtech, client, bot-project, hospitality, healthcare]
---

# [[Freshtech]] Bot Project - Client Meeting Notes

## Summary
Initial meeting with Freshtech regarding a bot development project. Initial requirements indicated a hotel bot starting March 10 with a $15K budget, but a follow-up email from their contact Priya clarified they now want a clinic bot with a $25K budget and April timeline—though this change is pending CTO confirmation.

## Key Details
- **Client:** Freshtech
- **Contact Person:** Priya (provided initial requirements and follow-up)
- **Project Type:** Originally specified as hotel bot; changed to clinic bot per Priya's follow-up
- **Original Timeline:** Contract start Monday, March 10 (3-month deal)
- **Revised Timeline:** End of April (pending confirmation)
- **Original Budget:** $15K
- **Revised Budget:** $25K
- **Status:** Waiting on Freshtech's CTO to confirm the change from hotel bot to clinic bot

## Action Items
- [ ] Confirm bot type (hotel vs. clinic) with Priya or Freshtech CTO
- [ ] Verify final budget ($15K or $25K)
- [ ] Clarify timeline (March 10 start vs. end of April)
- [ ] Obtain formal requirements for whichever bot type is approved

## Notes on Data Quality
**CONFLICTS DETECTED:** The follow-up email from Priya directly contradicts the original meeting notes:
- Bot type changed from "hotel bot" to "clinic bot"
- Budget increased from $15K to $25K
- Start date shifted from March 10 to end of April

These changes have NOT been confirmed—note says "waiting on their CTO to confirm." Do not proceed with development until CTO confirmation is received. Recommend seeking written confirmation of final requirements before proceeding.

## Related
- [[Priya (Freshtech Contact)]]
- [[Freshtech CTO (unconfirmed)]]
