# Beginner Guide

This repository is intended for users who are learning how to work with public market data in Python.

## Core workflow

1. Collect public data or load a small CSV.
2. Normalize columns into a simple OHLCV format.
3. Clean timestamps and numeric fields.
4. Calculate returns.
5. Export the result to CSV.
6. Review outputs manually.

## What this project does not do

- It does not trade.
- It does not manage accounts.
- It does not require exchange API keys.
- It does not provide financial advice.

## Recommended learning path

```bash
python examples/candle_cleaning_demo.py
python examples/returns_demo.py
kr-data sample --out sample_returns.csv
```
## Next steps

Future examples may cover Korean stock-market session handling, public CSV fixtures, and simple comparisons between local-market and global-market data.
