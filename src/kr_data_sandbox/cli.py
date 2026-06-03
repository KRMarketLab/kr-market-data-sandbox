from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path
from .candles import Candle, candles_to_frame, clean_ohlcv
from .csv_utils import write_csv
from .returns import add_returns

def sample_command(out: str) -> None:
    candles = [
        Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 100, 101, 99, 100, 1000),
        Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 100, 103, 100, 102, 1200),
        Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 102, 105, 101, 104, 1500),
    ]
    frame = candles_to_frame(candles)
    frame = clean_ohlcv(frame)
    frame = add_returns(frame)
    write_csv(frame, Path(out))
    print(f"Wrote sample market-data CSV to {out}")

def main() -> None:
    parser = argparse.ArgumentParser(description="KR market data sandbox")
    sub = parser.add_subparsers(dest="command", required=True)
    sample = sub.add_parser("sample", help="write a sample CSV with returns")
    sample.add_argument("--out", default="sample_returns.csv")
    args = parser.parse_args()
    if args.command == "sample":
        sample_command(args.out)

if __name__ == "__main__":
    main()
