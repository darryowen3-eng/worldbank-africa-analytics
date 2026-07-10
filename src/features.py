import pandas as pd

df = pd.read_csv("data/cleaned/worldbank_clean.csv")

df["gdp_per_capita"] = (
    df["gdp"] /
    df["population"]
)

df["population_millions"] = (
    df["population"] / 1_000_000
)

df["gdp_billions"] = (
    df["gdp"] / 1_000_000_000
)

df["high_unemployment"] = (
    df["unemployment"] > df["unemployment"].mean()
)

df["high_inflation"] = (
    df["inflation"] > df["inflation"].mean()
)

df["development_score"] = (
    (
        df["life_expectancy"] +
        df["literacy"]
    )
    /
    (
        df["unemployment"] +
        df["inflation"]
    )
)

df.to_csv(
    "data/cleaned/worldbank_features.csv",
    index=False
)

print(df.head())
