import pandas as pd

df = pd.read_csv("data/cleaned/worldbank_clean.csv")

report = {}

report["Rows"] = len(df)

report["Columns"] = len(df.columns)

report["Missing Values"] = df.isnull().sum().sum()

report["Duplicate Rows"] = df.duplicated().sum()

report["Countries"] = df["country"].nunique()

report["Years"] = df["date"].nunique()

report["Numeric Columns"] = (
    df.select_dtypes(include="number")
    .columns
    .tolist()
)

report["Categorical Columns"] = (
    df.select_dtypes(exclude="number")
    .columns
    .tolist()
)

print("\n========== DATA PROFILE ==========\n")

for key, value in report.items():
    print(f"{key}:")
    print(value)
    print()

print("========== SUMMARY STATISTICS ==========\n")

print(df.describe())

print("\n========== MISSING VALUES ==========\n")

print(df.isnull().sum())

print("\n========== DATA TYPES ==========\n")

print(df.dtypes)
