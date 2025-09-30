from fredapi import Fred
from dotenv import load_dotenv
import os, pandas as pd

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

ids = {"10Y": "DGS10", "2Y": "DGS2", "3M": "DGS3MO"}
df = pd.concat({k: fred.get_series(v) for k, v in ids.items()}, axis=1).sort_index()
df["10Y_minus_2Y"] = df["10Y"] - df["2Y"]
df["10Y_minus_3M"] = df["10Y"] - df["3M"]

df.to_csv("treasury_yields.csv", index=True)
print("Saved treasury_yields.csv with", len(df), "rows")
