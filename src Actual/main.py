from config import BacktestConfig, TICKERS
from data.data_loader import load_price_data
from engine.backtester import run_backtest
from analytics.metrics import compute_basic_metrics
from reporting.report import print_report

def main():
    # Explicit template guard
    if len(TICKERS) != 0:
        raise RuntimeError("This template repo must ship with ZERO tickers. Remove tickers to use template mode.")

    cfg = BacktestConfig()

    prices = load_price_data(TICKERS, cfg.start, cfg.end)
    equity_df = run_backtest(prices, cfg.initial_cash, cfg.rebalance_frequency)

    metrics = compute_basic_metrics(equity_df["equity"])
    print_report(equity_df, metrics)

if __name__ == "__main__":
    main()
