import pandas as pd
import numpy as np
from datetime import date

def load_price_data(tickers: list[str], start: date, end: date) -> pd.DataFrame:
    """
    TEMPLATE STUB:
    - In the real system, this would pull from yfinance, polygon, bloomberg, etc.
    - Here we return a dummy price series so the pipeline runs without tickers.

    Returns a DataFrame indexed by date with columns = tickers (or a dummy column).
    """
    idx = pd.date_range(start=start, end=end, freq="B")

    if len(tickers) == 0:
        # Dummy placeholder series so the engine can still demonstrate structure
        prices = pd.DataFrame(
            {"DUMMY_ASSET": 100.0 + np.cumsum(np.random.normal(0, 1, len(idx)))},
            index=idx,
        )
        return prices

    # If someone adds tickers later, this is where real integration would occur.
    raise NotImplementedError("Real ticker-based loading is intentionally not included in this template.")
