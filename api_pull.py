from fredapi import Fred
from dotenv import load_dotenv
import os
import pandas as pd

# 1) load API key from .env
load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# 2) pull series (added 30Y)
ids = {"30Y": "DGS30", "10Y": "DGS10", "2Y": "DGS2", "3M": "DGS3MO"}
df = pd.concat({k: fred.get_series(v) for k, v in ids.items()}, axis=1).sort_index()

# 3) add spreads (for inversion analysis)
df["10Y_minus_2Y"] = df["10Y"] - df["2Y"]
df["10Y_minus_3M"] = df["10Y"] - df["3M"]
# Optional extra with 30Y:
# df["30Y_minus_10Y"] = df["30Y"] - df["10Y"]

# 4) save
df.to_csv("treasury_yields.csv", index=True)
print("Saved treasury_yields.csv with", len(df), "rows")
