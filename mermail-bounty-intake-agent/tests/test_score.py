import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).parents[1] / "skills" / "mermail-bounty-intake-agent" / "scripts" / "score.py"
spec = importlib.util.spec_from_file_location("score_module", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ScoreTests(unittest.TestCase):
    def test_expected_value(self):
        result = module.score({
            "reward_max_usd": 500,
            "p_complete": 0.8,
            "p_win_given_complete": 0.25,
            "cash_cost_usd": 0,
            "human_minutes": 30,
            "confidence_haircut": 0.75,
        })
        self.assertEqual(result["expected_profit_usd"], 100.0)
        self.assertEqual(result["risk_adjusted_ev_usd"], 75.0)
        self.assertEqual(result["risk_adjusted_ev_per_human_hour_usd"], 150.0)

    def test_cost_can_make_ev_negative(self):
        result = module.score({
            "reward_max_usd": 100,
            "p_complete": 0.5,
            "p_win_given_complete": 0.2,
            "cash_cost_usd": 25,
            "human_minutes": 10,
            "confidence_haircut": 1,
        })
        self.assertEqual(result["expected_profit_usd"], -15.0)

    def test_invalid_probability_rejected(self):
        with self.assertRaises(ValueError):
            module.score({
                "reward_max_usd": 100,
                "p_complete": 1.2,
                "p_win_given_complete": 0.5,
            })

if __name__ == "__main__":
    unittest.main()
