#!/usr/bin/env python3
"""
Worm Leveraged Prediction Market Mathematical Risk & Hedging Engine
Engineered for Superteam Earn: Create Content on Premier League Predictions with worm ($500 USDC)
Listing: https://earn.superteam.fun/listings/bounties/create-content-on-premier-league-predictions-with-worm

Core Mechanics of worm.wtf:
1. Leveraged prediction markets on Solana (up to 3x leverage).
2. Dynamic outcome probability pricing.
3. Liquidation buffer modeling under high-volatility sports and crypto events.
4. Kelly Criterion capital allocation for optimal EV maximization.
"""

from typing import Dict, Any

class WormLeverageCalculator:
    def __init__(self, maintenance_margin_pct: float = 5.0):
        self.maintenance_margin = maintenance_margin_pct / 100.0

    def calculate_kelly_stake(self, estimated_prob: float, market_price: float, bankroll_usdc: float) -> Dict[str, Any]:
        """
        Calculates optimal fraction of bankroll to wager using the Kelly Criterion:
        f* = (b*p - q) / b
        where b = (1/market_price) - 1 is the net odds.
        """
        if not (0.01 <= estimated_prob <= 0.99) or not (0.01 <= market_price <= 0.99):
            raise ValueError("Probabilities and market prices must be between 0.01 and 0.99")
        if bankroll_usdc <= 0:
            raise ValueError("Bankroll must be strictly positive")

        net_odds = (1.0 / market_price) - 1.0
        q = 1.0 - estimated_prob
        
        kelly_fraction = (net_odds * estimated_prob - q) / net_odds
        # Half-Kelly for risk mitigation in volatile prediction markets
        conservative_fraction = max(0.0, kelly_fraction * 0.5)
        recommended_stake = round(bankroll_usdc * conservative_fraction, 2)

        is_positive_ev = kelly_fraction > 0

        return {
            "estimated_prob": estimated_prob,
            "market_price": market_price,
            "net_odds": round(net_odds, 3),
            "full_kelly_fraction": round(kelly_fraction, 4),
            "half_kelly_fraction": round(conservative_fraction, 4),
            "is_positive_ev": is_positive_ev,
            "recommended_stake_usdc": recommended_stake
        }

    def calculate_position(self, stake_usdc: float, entry_price: float, leverage: float) -> Dict[str, Any]:
        """
        Calculates position value, potential payout, and liquidation price for up to 3x leverage.
        """
        if stake_usdc <= 0:
            raise ValueError("Stake must be positive")
        if not (1.0 <= leverage <= 3.0):
            raise ValueError("Leverage on worm.wtf must be between 1.0x and 3.0x")
        if not (0.01 <= entry_price <= 0.99):
            raise ValueError("Entry price must be between 0.01 and 0.99")

        effective_exposure = stake_usdc * leverage
        shares = effective_exposure / entry_price

        # Max payout if outcome occurs ($1.00 settlement)
        gross_payout_usdc = shares * 1.0
        net_profit_usdc = gross_payout_usdc - stake_usdc - (stake_usdc * (leverage - 1.0))
        roi_percent = round((net_profit_usdc / stake_usdc) * 100.0, 1)

        # Liquidation price: when loss equals margin minus maintenance buffer
        # Loss = (entry_price - current_price) * shares = stake * (1 - maintenance_margin)
        max_loss_usdc = stake_usdc * (1.0 - self.maintenance_margin)
        drop_per_share = max_loss_usdc / shares
        liquidation_price = max(0.001, round(entry_price - drop_per_share, 4))

        return {
            "stake_usdc": stake_usdc,
            "leverage": leverage,
            "entry_price": entry_price,
            "effective_exposure_usdc": round(effective_exposure, 2),
            "shares_contract": round(shares, 4),
            "gross_payout_usdc": round(gross_payout_usdc, 2),
            "net_profit_usdc": round(net_profit_usdc, 2),
            "roi_percent": roi_percent,
            "liquidation_price": liquidation_price
        }
