import pandas as pd
from .portfolio import Portfolio

def generate_target_weights(prices_row: pd.Series) -> dict[str, float]:
    """
    TEMPLATE STRATEGY:
    - If only DUMMY_ASSET exists, allocate 100% to it.
    - Real strategy logic is intentionally omitted.
    """
    cols = list(prices_row.index)
    if "DUMMY_ASSET" in cols:
        return {"DUMMY_ASSET": 1.0}
    # If real symbols exist later, you would compute weights here
    return {}

def run_backtest(prices: pd.DataFrame, initial_cash: float, rebalance_frequency: str) -> pd.DataFrame:
    """
    Returns an equity curve DataFrame with columns:
    - equity
    """
    portfolio = Portfolio(initial_cash=initial_cash)

    # rebalance dates (template)
    rebalance_dates = set(prices.resample(rebalance_frequency).last().index)

    equity = []
    for dt, row in prices.iterrows():
        if dt in rebalance_dates:
            w = generate_target_weights(row)
            portfolio.rebalance_to_weights(row, w)

        equity.append({"date": dt, "equity": portfolio.value(row)})

    return pd.DataFrame(equity).set_index("date")
