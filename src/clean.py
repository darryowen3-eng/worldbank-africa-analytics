import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/worldbank_africa.csv")

print(df.info())

duplicates = df.duplicated().sum()

missing = df.isnull().sum()

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

numeric = [
    "gdp",
    "population",
    "inflation",
    "poverty",
    "unemployment",
    "life_expectancy",
    "literacy"
]

for col in numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df[numeric] = df[numeric].fillna(
    df.groupby("country")[numeric].transform("mean")
)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    ["country", "date"]
)

df.to_csv(
    "data/cleaned/worldbank_clean.csv",
    index=False
)

report = {
    "Rows": len(df),
    "Columns": len(df.columns),
    "Duplicates": duplicates,
    "Missing Values": missing,
    "Countries": df["country"].nunique(),
    "Years": df["date"].nunique()
}

print()

for k, v in report.items():
    print(k, "\n", v)
