from __future__ import annotations
from datetime import datetime, timezone
from kr_data_sandbox.candles import Candle, candles_to_frame
from kr_data_sandbox.returns import add_returns

candles = [
    Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 100, 101, 99, 100),
    Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 100, 102, 99, 101),
    Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 101, 104, 100, 103),
]
frame = candles_to_frame(candles)
print(add_returns(frame).to_string(index=False))
