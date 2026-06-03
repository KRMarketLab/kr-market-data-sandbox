from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
import pandas as pd
import requests
from kr_data_sandbox.candles import clean_ohlcv
from kr_data_sandbox.returns import add_returns

def fetch_public_binance_klines(symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 10) -> pd.DataFrame:
    """Small public-data example. This does not require API keys and does not place orders."""
    url = "https://api.binance.com/api/v3/klines"
    response = requests.get(url, params={"symbol": symbol.upper(), "interval": interval, "limit": limit}, timeout=10)
    response.raise_for_status()
    rows: list[dict[str, Any]] = []
    for item in response.json():
        rows.append({
            "timestamp": datetime.fromtimestamp(item[0] / 1000, tz=timezone.utc),
            "open": item[1], "high": item[2], "low": item[3], "close": item[4], "volume": item[5],
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    frame = fetch_public_binance_klines()
    frame = clean_ohlcv(frame)
    frame = add_returns(frame)
    print(frame.tail().to_string(index=False))
