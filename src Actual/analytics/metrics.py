import pandas as pd
import numpy as np

def compute_basic_metrics(equity_curve: pd.Series) -> dict[str, float]:
    rets = equity_curve.pct_change().dropna()
    if len(rets) == 0:
        return {"cagr": 0.0, "vol": 0.0, "sharpe": 0.0, "max_drawdown": 0.0}

    # annualization assumptions (template)
    ann_factor = 252.0
    avg = rets.mean() * ann_factor
    vol = rets.std(ddof=1) * np.sqrt(ann_factor)
    sharpe = (avg / vol) if vol > 0 else 0.0

    peak = equity_curve.cummax()
    dd = (equity_curve / peak) - 1.0
    max_dd = float(dd.min())

    # template CAGR
    years = len(equity_curve) / 252.0
    cagr = (equity_curve.iloc[-1] / equity_curve.iloc[0]) ** (1 / years) - 1 if years > 0 else 0.0

    return {
        "cagr": float(cagr),
        "vol": float(vol),
        "sharpe": float(sharpe),
        "max_drawdown": float(max_dd),
    }
