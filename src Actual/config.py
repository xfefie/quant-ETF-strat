from dataclasses import dataclass
from datetime import date

# EXPLICITLY EMPTY: this repo intentionally contains NO tickers.
TICKERS: list[str] = []

@dataclass(frozen=True)
class BacktestConfig:
    start: date = date(2020, 1, 1)
    end: date = date(2021, 1, 1)
    initial_cash: float = 100_000.0
    rebalance_frequency: str = "M"  # D/W/M/Q (template only)
    allow_short: bool = False
