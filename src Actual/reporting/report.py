import pandas as pd

def print_report(equity_df: pd.DataFrame, metrics: dict[str, float]) -> None:
    last = equity_df["equity"].iloc[-1]
    first = equity_df["equity"].iloc[0]
    print("\n=== TEMPLATE REPORT ===")
    print(f"Start Equity: {first:,.2f}")
    print(f"End Equity:   {last:,.2f}")
    print("\nMetrics:")
    for k, v in metrics.items():
        print(f"- {k}: {v:.4f}")
