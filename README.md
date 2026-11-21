# Worm.wtf Prediction Markets: Quantitative Hedging & Leverage Model

Mathematical risk engine, fractional Kelly criterion position sizer, and liquidation corridor simulator for **Worm** (`@wormwtf`) — Solana's premier leveraged sports prediction market.

## Overview
Worm introduces up to 3× leverage on Premier League matches and live events on Solana. While leverage magnifies upside on favorable outcomes, rigorous downside risk management is essential.

This repository contains:
1. **Quantitative Risk Engine (`hedging_model.py`)**:
   - Calculates exact gross and net payouts on leveraged outcome contracts.
   - Computes liquidation price corridors based on entry market implied probability and margin maintenance.
   - Sizes positions using the fractional Kelly Criterion: $f^* = \frac{b \cdot p - q}{b}$.
2. **Unit Test Suite (`test_hedging_model.py`)**: 4/4 passing unit tests verifying mathematical invariants.
3. **Publication-Ready Distribution Thread (`SUBMISSION_THREAD.md`)**: 5-part technical thread ready for X (Twitter).
4. **Live Interactive Web Calculator**: [https://wormpredictcalc.vercel.app](https://wormpredictcalc.vercel.app).

## Quickstart & Verification
```bash
python3 -m unittest test_hedging_model.py
python3 hedging_model.py
```

## Live Calculator
👉 **[https://wormpredictcalc.vercel.app](https://wormpredictcalc.vercel.app)**
