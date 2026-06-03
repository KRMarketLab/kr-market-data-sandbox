from __future__ import annotations
import pandas as pd
from kr_data_sandbox.candles import add_basic_candle_checks, clean_ohlcv

raw = pd.DataFrame([
    {"timestamp": "2026-01-01 01:00:00+00:00", "open": "101", "high": "103", "low": "100", "close": "102", "volume": "1200"},
    {"timestamp": "2026-01-01 00:00:00+00:00", "open": "100", "high": "101", "low": "99", "close": "100", "volume": "1000"},
    {"timestamp": "2026-01-01 01:00:00+00:00", "open": "101", "high": "104", "low": "100", "close": "103", "volume": "1300"},
    {"timestamp": "bad timestamp", "open": "bad", "high": "bad", "low": "bad", "close": "bad", "volume": "0"},
])
cleaned = clean_ohlcv(raw)
checked = add_basic_candle_checks(cleaned)
print(checked.to_string(index=False))
