# Data Sources

This project is designed around public, keyless data examples.

## Example source types

- Public exchange OHLCV endpoints
- Manually downloaded CSV files
- Synthetic sample data for testing
- Research datasets that permit redistribution

## Design principle

Keep source adapters separate from analysis logic. This makes it easier to test data-cleaning and return calculations without depending on live network calls.

## Caution

Public market data can be delayed, incomplete, rate-limited, or inaccurate. Always validate important calculations independently.
