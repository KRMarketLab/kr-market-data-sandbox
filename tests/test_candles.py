import pandas as pd
from kr_data_sandbox.candles import add_basic_candle_checks, clean_ohlcv

def test_clean_ohlcv_sorts_and_deduplicates():
    frame = pd.DataFrame([
        {"timestamp": "2026-01-01 01:00:00+00:00", "open": 101, "high": 103, "low": 100, "close": 102},
        {"timestamp": "2026-01-01 00:00:00+00:00", "open": 100, "high": 101, "low": 99, "close": 100},
        {"timestamp": "2026-01-01 01:00:00+00:00", "open": 101, "high": 104, "low": 100, "close": 103},
    ])
    cleaned = clean_ohlcv(frame)
    assert len(cleaned) == 2
    assert cleaned.iloc[-1]["close"] == 103

def test_add_basic_candle_checks():
    frame = pd.DataFrame([{"timestamp": "2026-01-01", "open": 100, "high": 101, "low": 99, "close": 100}])
    checked = add_basic_candle_checks(frame)
    assert bool(checked.iloc[0]["is_valid_ohlc"]) is True
