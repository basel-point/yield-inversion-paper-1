import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV we created earlier; first column is the date index
df = pd.read_csv("treasury_yields.csv", index_col=0, parse_dates=True)

# Optional: focus on modern period for readability
# df = df.loc["1990":]

fig = plt.figure(figsize=(10, 5))
plt.plot(df.index, df["10Y_minus_2Y"], label="10Y - 2Y")
plt.plot(df.index, df["10Y_minus_3M"], label="10Y - 3M")
plt.axhline(0, linewidth=1)
plt.title("Yield Curve Spreads (10Y−2Y, 10Y−3M)")
plt.xlabel("Date")
plt.ylabel("Percentage Points")
plt.legend()
plt.tight_layout()
plt.savefig("spreads.png", dpi=150)
print("Saved spreads.png")
