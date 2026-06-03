from __future__ import annotations
from pathlib import Path
import pandas as pd

def read_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)

def write_csv(frame: pd.DataFrame, path: str | Path) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
