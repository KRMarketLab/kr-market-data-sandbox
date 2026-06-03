import pandas as pd
import pytest
from kr_data_sandbox.returns import add_returns, pct_return, rolling_change_pct

def test_pct_return():
    assert pct_return(110, 100) == pytest.approx(10.0)

def test_add_returns():
    frame = pd.DataFrame({"close": [100, 105, 110]})
    result = add_returns(frame)
    assert result.loc[1, "return_pct"] == pytest.approx(5.0)
    assert result.loc[2, "cumulative_return_pct"] == pytest.approx(10.0)

def test_rolling_change_pct():
    frame = pd.DataFrame({"close": [100, 105, 110]})
    result = rolling_change_pct(frame, window=2)
    assert result.iloc[2] == pytest.approx(10.0)
