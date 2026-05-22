# VECM Statistical Arbitrage Engine

A multivariate statistical arbitrage system built using Johansen Cointegration techniques and mean-reversion trading logic across a basket of correlated technology stocks.

The project identifies long-term equilibrium relationships between assets, constructs a cointegrated spread, generates Z-score trading signals, and evaluates strategy performance using backtesting metrics such as Sharpe Ratio and Maximum Drawdown.

---

# Features

- Johansen Cointegration Test
- Cointegrated Spread Construction
- Z-Score Signal Generation
- Mean Reversion Trading Logic
- Long/Short Signal System
- Rolling Cointegration Rank Monitoring
- Backtesting Engine
- Sharpe Ratio Calculation
- Maximum Drawdown Analysis
- Data Visualization

---

# Econometric Logic

The system uses the Johansen Cointegration Test to identify equilibrium relationships between multiple assets.

A cointegration vector is extracted to construct a synthetic spread. Since cointegrated spreads tend to revert toward equilibrium, the spread is normalized into a Z-score.

Trading signals are generated based on mean-reversion thresholds:

- Z-Score > 2 → Short Spread
- Z-Score < -2 → Long Spread
- |Z-Score| < 0.5 → Exit Position

The project also computes rolling cointegration ranks to monitor whether the equilibrium relationship between assets remains stable over time.

---

# Backtesting Logic

The strategy simulates statistical arbitrage trades using spread changes over time.

The backtester includes:

- Transaction Costs
- Borrow Costs for Short Positions
- Cumulative Return Tracking
- Sharpe Ratio Evaluation
- Maximum Drawdown Measurement

Strategy returns are accumulated through time to evaluate the effectiveness of the mean-reversion system.

---

# Rolling Cointegration Rank Monitoring

The project implements rolling window validation using Johansen rank estimation across time windows.

This helps monitor whether the equilibrium relationship between assets remains stable through time.

If the rolling cointegration rank collapses, the system flags a potential cointegration breakdown and warns about unstable market relationships.

---

# Tech Stack

- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- yFinance

---

# Project Structure

```text
vecm-arb/
│
├── graphs/
│   ├── Stock Prices.png
│   ├── Spread Analysis.png
│   ├── Z Score.png
│   ├── Strategy Performance.png
│   └── Rolling rank.png
│
├── main.py
├── data_loader.py
├── cointegration.py
├── signals.py
├── backtester.py
├── rank_monitor.py
├── plotting.py
├── requirements.txt
└── README.md
```

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Output Graphs

## Stock Prices

![Stock Prices](graphs/Stock%20Prices.png)

---

## Spread Analysis

![Spread Analysis](graphs/Spread%20Analysis.png)

---

## Z Score

![Z Score](graphs/Z%20Score.png)

---

## Strategy Performance

![Strategy Performance](graphs/Strategy%20Performance.png)

---

## Rolling Cointegration Rank

![Rolling Rank](graphs/Rolling%20rank.png)

---

# Repository Goals

This repository demonstrates:

- Multivariate cointegration analysis
- Statistical arbitrage signal generation
- Mean-reversion based trading systems
- Basic quantitative backtesting workflows
- Rolling stability validation of equilibrium relationships

The project focuses on building a clean and modular research-oriented prototype for statistical arbitrage experimentation.

---

# Notes

This project is intended for educational and research purposes only.

It is not designed for live trading or financial advice.
