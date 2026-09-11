# Opportunity scoring

The goal is to maximize expected profit while minimizing required human attention.

For each opportunity estimate:

- `reward_max_usd`: maximum plausible payout for this submission.
- `p_complete`: probability the agent/user can produce a compliant submission.
- `p_win_given_complete`: probability a compliant submission receives the payout.
- `cash_cost_usd`: required out-of-pocket cost.
- `human_minutes`: expected user review/approval time.
- `ai_hours`: expected agent execution time.

Compute:

```text
expected_profit_usd = reward_max_usd * p_complete * p_win_given_complete - cash_cost_usd
```

Confidence haircut:
- 1.00 — official source, clear rubric, clear submission path
- 0.75 — one material unknown
- 0.50 — multiple material unknowns
- 0.25 — reward/payment or submission path unverified

```text
risk_adjusted_ev = expected_profit_usd * confidence_haircut
human_hours = max(human_minutes / 60, 0.25)
ev_per_human_hour = risk_adjusted_ev / human_hours
```

Never hide assumptions. If probabilities are estimates, label them as estimates.

Competition adjustments:
- explicit existing assignee or many active competing PRs -> reduce `p_win_given_complete`;
- winner-take-all contest with many entrants -> reduce it substantially;
- multiple paid places or per-accepted-item bounty -> increase it relative to a single prize;
- application restricted to a role/account the user does not have -> PASS.
