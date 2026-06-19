"""
SERVER LOg reader
"""

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "server.log"


df = pd.read_csv(DATA, parse_dates=["timestamp"], index_col="timestamp")
# df.loc (LableSlicer)
res = df.loc["2026-06-19 14:00":"2026-06-19 16:00"][df["level"] == "ERROR"]
print(res)
