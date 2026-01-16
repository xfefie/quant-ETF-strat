# quant-ETF-strat
Quant strat built by pre-approved complaint ETFs.


# Quant Portfolio Backtester (TEMPLATE / SKELETON)

⚠️ **Important disclaimer (read first):**
- This repository is a **template / structural skeleton** intended to show how the project is organized.
- **There are NO ETF tickers included anywhere in this repo** (ticker lists are intentionally empty).
- This is **NOT the full program**. It is missing production logic, real strategy rules, real data integrations, and full reporting/export.

## What this template includes
- A clean folder structure for a portfolio backtesting engine
- Placeholder modules for:
  - data ingestion
  - backtest loop
  - portfolio construction / rebalancing
  - performance metrics
  - reporting output
- A minimal runnable flow that demonstrates the “wiring” between components

## What this template does NOT include
- ✅ No tickers (explicitly empty lists)
- ✅ No trading signals or alpha logic
- ✅ No real brokerage/execution integration
- ✅ No real market data pulling by default (stubs only)
- ✅ No production risk model / constraints engine

---

## Repo Structure

# repo-root/
## README.md
## requirements.txt
## .env.example
## src/
### main.py
### config.py
### data/
#### data_loader.py
### engine/
#### backtester.py
#### portfolio.py
### analytics/
#### metrics.py
### reporting/
#### report.py
