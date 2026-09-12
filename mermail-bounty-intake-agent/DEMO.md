# 2-minute demo plan

## 0:00–0:20 — Problem

Show a Mermail inbox containing three paid-work messages: a legitimate development bounty, an attractive but unverified forwarded offer, and a malicious prompt-injection email asking for a wallet secret.

Say: "An agent inbox can receive opportunities continuously, but advertised reward is not expected profit, and email itself is untrusted."

## 0:20–0:55 — Safe Mermail intake

Run:

> Use $mermail-bounty-intake-agent to review the newest paid-work opportunities. Send nothing and spend nothing.

Show `list_mailboxes`, metadata-only `list_emails` / `search_emails`, and one bounded `get_email` for each selected candidate. Point out that the skill does not obey instructions embedded in the malicious message.

## 0:55–1:25 — Verification + scoring

Show the structured opportunity card and run:

```bash
python skills/mermail-bounty-intake-agent/scripts/score.py examples/opportunity.json
```

Explain that reward, eligibility, deadline, competition and required capital affect the score. An unverified high-dollar offer becomes VERIFY rather than GO.

## 1:25–1:50 — Human approval boundary

Show a useful reply draft such as a clarification question. The agent previews recipients, subject and body but does not call `send_email` until the human approves the exact message.

## 1:50–2:00 — Close

Show the ranked GO / VERIFY / PASS table and say: "Mermail provides the durable agent inbox; this skill turns it into a safe revenue pipeline optimized for expected value per minute of human attention."
