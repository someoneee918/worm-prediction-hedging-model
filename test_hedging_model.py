#!/usr/bin/env python3
"""
Unit Test Suite for Worm Prediction Market Risk & Hedging Engine
Tests:
1. Positive EV Kelly stake calculation
2. 3x Leverage position payout and liquidation pricing
3. 1x Leverage spot position behavior (no liquidation)
4. Out-of-bounds parameter validation
"""

import unittest
from hedging_model import WormLeverageCalculator

class TestWormLeverageCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = WormLeverageCalculator()

    def test_positive_ev_kelly(self):
        # Estimated prob = 60%, market price = 0.50 (implied 50%) -> Positive EV!
        res = self.calc.calculate_kelly_stake(0.60, 0.50, 1000.0)
        self.assertTrue(res["is_positive_ev"])
        self.assertEqual(res["full_kelly_fraction"], 0.20)
        self.assertEqual(res["recommended_stake_usdc"], 100.0) # Half-kelly: 10%

    def test_three_x_leverage_position(self):
        # 100 USDC at 0.50 entry with 3x leverage -> 300 USDC exposure (600 shares)
        res = self.calc.calculate_position(100.0, 0.50, 3.0)
        self.assertEqual(res["effective_exposure_usdc"], 300.0)
        self.assertEqual(res["gross_payout_usdc"], 600.0)
        # Net profit = 600 - 100 (stake) - 200 (borrowed) = 300 USDC (300% ROI)
        self.assertEqual(res["net_profit_usdc"], 300.0)
        self.assertEqual(res["roi_percent"], 300.0)
        # Liquidation: drop = (100 * 0.95) / 600 = 0.1583 -> Liquidation at ~0.3417
        self.assertLess(res["liquidation_price"], 0.50)
        self.assertGreater(res["liquidation_price"], 0.30)

    def test_one_x_spot_no_leverage(self):
        res = self.calc.calculate_position(100.0, 0.50, 1.0)
        self.assertEqual(res["net_profit_usdc"], 100.0)
        self.assertEqual(res["roi_percent"], 100.0)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_position(100.0, 0.50, 4.0) # Max leverage is 3.0x
        with self.assertRaises(ValueError):
            self.calc.calculate_kelly_stake(1.5, 0.50, 100.0)

if __name__ == "__main__":
    unittest.main()
