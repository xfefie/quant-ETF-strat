# quant-ETF-strat

A small portfolio backtester. The version in this repo is a template: the ETF list is empty, prices are a synthetic random walk, and the book holds that one series. Running it prints start and end equity plus four performance stats.

## Strategy

Settings are in `src Actual/config.py`.

- Window: 1 January 2020 through 1 January 2021
- Starting capital: $100,000
- Rebalance frequency: monthly (`M`)
- Short sales: disabled (`allow_short` is stored and unused)

`TICKERS` is an empty list. `main.py` raises if that list has any symbols, so the template runs only with no tickers.

On a rebalance date, `generate_target_weights` assigns 100% to `DUMMY_ASSET`. The portfolio liquidates to cash, then buys that weight in fractional shares. Fills use the same day's price. There are no commissions, no slippage, and no position limits.

The account stays in cash until the first month-end that is also a row in the price index, which in this window is 31 January 2020. After that fill the book is fully invested. Later rebalances target the same asset at the same weight, so with zero costs the share count stays put.

`resample("M")` labels each bin with the calendar month-end. A weekend month-end is not a row in the business-day index, so that month does not trade. In this window those dates are 29 February 2020, 31 May 2020, and 31 October 2020. 31 January 2021 is a Sunday and falls after the sample ends.

## Data

`load_price_data` builds one column, `DUMMY_ASSET`, for every business day from the start date through the end date: 263 rows, 1 January 2020 through 1 January 2021.

The price starts at 100 and adds an independent Normal(0, 1) shock each day. The draw is unseeded, so every run is a new path. Nothing is downloaded. Passing a non-empty ticker list raises `NotImplementedError`.

## How to run

Use Python 3.10 or newer. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd "src Actual"
python main.py
```

`main.py` imports `config`, `data`, `engine`, `analytics`, and `reporting` as top-level modules, so the working directory has to be `src Actual`. The source folder name includes a space.

Pandas 3 removed the `M` offset this config uses. `requirements.txt` keeps pandas on the 2.x line. Pandas 2.2 and 2.3 still run, and they print a `FutureWarning` about `M`.

A run prints:

```text
=== TEMPLATE REPORT ===
Start Equity: 100,000.00
End Equity:   ...

Metrics:
- cagr: ...
- vol: ...
- sharpe: ...
- max_drawdown: ...
```

## Backtest results

Start equity is always 100,000.00. End equity and the four stats depend on that run's random path. There is no saved result file.

The printed stats are:

| Stat | Definition |
| --- | --- |
| cagr | `(end / start) ** (1 / years) - 1`, with `years = number of rows / 252` |
| vol | Sample standard deviation of daily simple returns, times `sqrt(252)` |
| sharpe | Mean daily return times 252, divided by vol. No risk-free rate is subtracted |
| max_drawdown | Largest peak-to-trough decline on the equity curve |

Two back-to-back runs on 31 October 2026, shown as the script printed them (ratios, four decimals):

| Run | End equity | CAGR | Vol | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 101,674.84 | 0.0160 | 0.1448 | 0.1824 | -0.1208 |
| 2 | 81,869.10 | -0.1744 | 0.1440 | -1.2637 | -0.2374 |

Those rows show the report format and how far two draws can land from each other. The next run will print different numbers. Volatility clusters near 0.14 because the daily shock has a standard deviation of 1 on a price that starts at 100.

## Layout

```text
requirements.txt
README.md
src Actual/
  main.py                 entry point
  config.py               dates, cash, frequency, empty ticker list
  data/data_loader.py     synthetic price path
  engine/backtester.py    monthly loop and target weights
  engine/portfolio.py     cash, shares, and rebalance
  analytics/metrics.py    CAGR, vol, Sharpe, max drawdown
  reporting/report.py     printed summary
```
