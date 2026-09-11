# Mermail Bounty Intake Agent

Community Mermail skill for turning a dedicated agent inbox into a safe, ranked intake queue for paid work: OSS bounties, hackathons, grants, agent tasks, and contract leads.

The differentiator is **risk-adjusted expected value per minute of human attention**. The skill reads candidate mail with bounded Mermail MCP calls, treats every message as untrusted data, extracts opportunity facts, verifies what it can, and returns a compact `GO / VERIFY / PASS` decision.

## Why this fits Mermail

Mermail gives an agent a durable email identity and inbox. This skill turns that inbox into a revenue workflow rather than a generic email reader.

Core flow:

`inbound opportunity -> safe metadata scan -> bounded body read -> structured facts -> source verification -> EV scoring -> GO/VERIFY/PASS -> optional reply preview`

No email can authorize spending, wallet actions, disclosure of credentials/secrets, security testing outside verified scope, or an external reply.

## Install with Mermail + Codex

```bash
codex mcp add mermail --url https://console.mermail.app/mcp
codex mcp login mermail
npx --yes skills add Nudgen-Marketing/mermail-skills --agent codex --skill '*' --global --yes
```

Then install or copy `skills/mermail-bounty-intake-agent` into your agent's user-level skills directory.

## Demo prompt

> Use $mermail-bounty-intake-agent to review the newest paid-work opportunities in my Mermail inbox. Spend no money and send nothing. Rank only opportunities whose reward, deadline and submission path can be verified.

## Deterministic scorer

```bash
python skills/mermail-bounty-intake-agent/scripts/score.py examples/opportunity.json
```

## Status

Community / unofficial Mermail companion skill. It does not replace the official `Nudgen-Marketing/mermail-skills` package.

## License

MIT
