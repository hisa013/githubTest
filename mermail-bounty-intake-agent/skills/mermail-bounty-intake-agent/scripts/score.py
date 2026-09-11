#!/usr/bin/env python3
import json
import sys

def probability(value):
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("probability values must be between 0 and 1")
    return value

def score(data):
    reward = max(0.0, float(data["reward_max_usd"]))
    p_complete = probability(data["p_complete"])
    p_win = probability(data["p_win_given_complete"])
    cash_cost = max(0.0, float(data.get("cash_cost_usd", 0)))
    human_minutes = max(0.0, float(data.get("human_minutes", 0)))
    haircut = probability(data.get("confidence_haircut", 1.0))

    expected = reward * p_complete * p_win - cash_cost
    risk_adjusted = expected * haircut
    human_hours = max(human_minutes / 60.0, 0.25)

    return {
        "expected_profit_usd": round(expected, 2),
        "risk_adjusted_ev_usd": round(risk_adjusted, 2),
        "risk_adjusted_ev_per_human_hour_usd": round(risk_adjusted / human_hours, 2),
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: score.py opportunity.json")
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps(score(data), indent=2))

if __name__ == "__main__":
    main()
