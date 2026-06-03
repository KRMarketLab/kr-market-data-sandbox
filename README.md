# KR Market Data Sandbox

KR Market Data Sandbox is a beginner-friendly collection of keyless Python examples for collecting, cleaning, and analyzing public market data.

The project focuses on simple, reproducible research workflows for Korean market-related analysis. It is designed for learning and experimentation, not trading execution.

## Why this exists

Many market-data examples mix together data collection, cleaning, analysis, and trading logic. This repository keeps the scope small and safe:

- public data examples only,
- no private API keys,
- no live orders,
- simple candle and return calculations,
- CSV-based workflows that are easy to inspect,
- tests for core data-cleaning and return logic.

## Features

- Candle data model
- OHLCV cleaning helpers
- Return and cumulative-return calculations
- CSV loading and saving helpers
- Small sample-data examples
- Beginner-focused documentation

## Installation

```bash
git clone https://github.com/KRMarketLab/kr-market-data-sandbox.git
cd kr-market-data-sandbox
python -m pip install -e ".[dev]"
```

## Run examples

```bash
python examples/candle_cleaning_demo.py
python examples/returns_demo.py
```

## CLI

```bash
kr-data sample --out sample_returns.csv
```

## Related project

- [KR Equity Perp Gap Monitor](https://github.com/KRMarketLab/kr-equity-perp-gap-monitor): a gap-analysis toolkit built on normalized candle data.

## Safety and scope

This repository does not execute trades, access user accounts, handle private exchange keys, or provide financial advice. It is a public-data research and learning sandbox.

## License

MIT
