from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import pandas as pd

@dataclass(frozen=True)
class Candle:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0

REQUIRED_COLUMNS = ["timestamp", "open", "high", "low", "close"]

def candles_to_frame(candles: list[Candle]) -> pd.DataFrame:
    return pd.DataFrame([c.__dict__ for c in candles])

def clean_ohlcv(frame: pd.DataFrame) -> pd.DataFrame:
    """Clean a simple OHLCV DataFrame."""
    missing = [col for col in REQUIRED_COLUMNS if col not in frame.columns]
    if missing:
        raise ValueError(f"missing required columns: {missing}")
    cleaned = frame.copy()
    cleaned["timestamp"] = pd.to_datetime(cleaned["timestamp"], utc=True, errors="coerce")
    numeric_cols = ["open", "high", "low", "close", "volume"]
    for col in numeric_cols:
        if col in cleaned.columns:
            cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")
    cleaned = cleaned.dropna(subset=["timestamp", "open", "high", "low", "close"])
    cleaned = cleaned.sort_values("timestamp").drop_duplicates("timestamp", keep="last")
    return cleaned.reset_index(drop=True)

def add_basic_candle_checks(frame: pd.DataFrame) -> pd.DataFrame:
    """Add simple validation flags for OHLC data quality review."""
    checked = frame.copy()
    checked["high_is_valid"] = checked["high"] >= checked[["open", "close", "low"]].max(axis=1)
    checked["low_is_valid"] = checked["low"] <= checked[["open", "close", "high"]].min(axis=1)
    checked["is_valid_ohlc"] = checked["high_is_valid"] & checked["low_is_valid"]
    return checked
