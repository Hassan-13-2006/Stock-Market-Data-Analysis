
import pandas as pd

df = pd.read_csv("AAPL_Cleaned_Data.csv")

df["Previous_Close"] = df["Close"].shift(1)

df["Overnight_Gap_%"] = (
    (df["Open"] - df["Previous_Close"])
    / df["Previous_Close"] * 100
)

df["Intraday_Return_%"] = (
    (df["Close"] - df["Open"])
    / df["Open"] * 100
)

row = df[df["Date"].str.startswith("2000-09-29")]

print(row[[
    "Date", "Previous_Close", "Open", "Close",
    "Overnight_Gap_%", "Intraday_Return_%"
]].to_string(index=False))

print("\nDATA QUALITY NOTE")
print("Date: 2000-09-29")
print("Close-to-close return: -51.87%")
print("Overnight gap: -47.31%")
print("Intraday return: -8.65%")
print("Status: Requires historical price-adjustment verification.")

