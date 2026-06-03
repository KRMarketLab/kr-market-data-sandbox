from __future__ import annotations
import pandas as pd

def pct_return(current: float, base: float) -> float:
    if base == 0:
        raise ValueError("base must not be zero")
    return (current / base - 1.0) * 100.0

def add_returns(frame: pd.DataFrame, price_col: str = "close") -> pd.DataFrame:
    if price_col not in frame.columns:
        raise ValueError(f"missing price column: {price_col}")
    result = frame.copy()
    result["return_pct"] = result[price_col].pct_change() * 100.0
    first_valid = result[price_col].dropna()
    if first_valid.empty:
        result["cumulative_return_pct"] = pd.NA
        return result
    base = float(first_valid.iloc[0])
    result["cumulative_return_pct"] = (result[price_col] / base - 1.0) * 100.0
    return result

def rolling_change_pct(frame: pd.DataFrame, window: int, price_col: str = "close") -> pd.Series:
    if window < 1:
        raise ValueError("window must be at least 1")
    if price_col not in frame.columns:
        raise ValueError(f"missing price column: {price_col}")
    return frame[price_col].pct_change(periods=window) * 100.0
