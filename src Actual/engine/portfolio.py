import pandas as pd

class Portfolio:
    def __init__(self, initial_cash: float):
        self.cash = float(initial_cash)
        self.positions = {}  # symbol -> shares

    def value(self, prices_row: pd.Series) -> float:
        pos_value = 0.0
        for sym, shares in self.positions.items():
            if sym in prices_row:
                pos_value += shares * float(prices_row[sym])
        return self.cash + pos_value

    def rebalance_to_weights(self, prices_row: pd.Series, target_weights: dict[str, float]) -> None:
        """
        TEMPLATE:
        - No transaction costs, no slippage, no constraints.
        - Naive rebalance using current portfolio value.
        """
        total_value = self.value(prices_row)
        if total_value <= 0:
            return

        # Liquidate everything (template-simple)
        self.positions = {}
        self.cash = total_value

        # Buy new weights
        for sym, w in target_weights.items():
            if sym not in prices_row:
                continue
            px = float(prices_row[sym])
            if px <= 0:
                continue
            dollars = total_value * float(w)
            shares = dollars / px
            self.positions[sym] = shares

        # Remaining cash (template ignores rounding)
        invested = sum(
            self.positions[s] * float(prices_row[s])
            for s in self.positions
            if s in prices_row
        )
        self.cash = total_value - invested
