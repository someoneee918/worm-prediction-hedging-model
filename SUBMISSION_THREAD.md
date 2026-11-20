# Worm.wtf Prediction Markets: Quantitative Leverage & Hedging Engine

**Target Opportunity:** [Superteam Earn - Create Content on Premier League Predictions with worm ($500 USDC)](https://earn.superteam.fun/listings/bounties/create-content-on-premier-league-predictions-with-worm)  
**Sponsor:** worm (`@wormwtf`) on Solana  
**Prizes:** $500 USDC Locked Pool (1st: 150 USDC, 2nd: 75 USDC, 3rd: 50 USDC, 4th: 25 USDC, 20 spots for 20 USDC)  
**Solana Payout Wallet:** `DW2MdHEq3qZ6nh9b5YFUoaPnBuuxC8Gz2785kwbbjSAM`  
**Base EVM Payout Wallet:** `0xF0E0D361bBE899F3089f0a968506eF2B97693c01`  
**Status:** Tested, 4/4 Unit Tests Passing, Edge Visualizer Deployed  

---

## 1. Copy-Ready 5-Post X (Twitter) Thread

### Post 1 (The Hook: Prediction Markets Meet Leverage)
```
Prediction markets like Polymarket showed the world that collective intelligence beats pundits.

Now @wormwtf is bringing the missing ingredient to Solana:
Up to 3× leverage on Premier League matches and live events. 🪱⚽

Here is how the quantitative math behind leveraged prediction markets works 🧵👇
```

### Post 2 (How Leveraged Outcome Shares Work)
```
2/ On standard prediction platforms, buying an outcome trading at $0.40 yields $1.00 at resolution (150% ROI).

On @wormwtf, you can back your conviction with up to 3× leverage:
• 100 USDC margin with 3× leverage controls 300 USDC of outcome contracts (750 shares).
• When your team wins, your gross payout is $750.
• Net profit: $450 on a $100 initial stake (450% ROI). 📈
```

### Post 3 (Managing the Liquidation Corridor)
```
3/ Leverage amplifies upside, but precision risk management is mandatory.

In our quantitative model (`hedging_model.py`):
With 3× leverage at $0.40 entry, your liquidation threshold sits at ~$0.27.
If match momentum drops the market probability below 27%, margin is liquidated.

Smart traders size stakes using the fractional Kelly Criterion: f* = (b*p - q) / b 🧠
```

### Post 4 (Solana-Speed & Real USDC Payouts)
```
4/ Why does this matter on @solana?
In sports, odds change in milliseconds when a goal is scored.

• @wormwtf settles orders instantly with sub-cent transaction fees.
• Referral program pays 30% of trading fees in USDC directly to your wallet for 90 days.
• Weekly prize pools (e.g. $1,500 USDC Matchweek pools) reward the top 10 traders. ⚡
```

### Post 5 (Explore the Markets & Interactive Calculator)
```
5/ Don't just watch the Premier League—trade the probabilities.

Explore active markets for every match:
👉 https://www.worm.wtf/sports?league=eng.1

Test your leverage, ROI, and liquidation prices before trading with our interactive calculator:
👉 https://wormpredictcalc.vercel.app

Follow @wormwtf and join the next generation of Solana prediction markets! 🪱⚽
```

---

## 2. Submission Steps
1. Follow `@wormwtf` on Twitter/X.
2. Connect your Solana wallet (`DW2MdHEq3qZ6nh9b5YFUoaPnBuuxC8Gz2785kwbbjSAM`) to `worm.wtf` and grab your referral link under the "Earn" button.
3. Post the 5-tweet thread on Twitter/X tagging `@wormwtf` and include your referral link.
4. Submit the tweet link on the [Superteam Bounty Page](https://earn.superteam.fun/listings/bounties/create-content-on-premier-league-predictions-with-worm) with payout to `DW2MdHEq3qZ6nh9b5YFUoaPnBuuxC8Gz2785kwbbjSAM`.
