import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/worldbank_clean.csv")

latest = (
    df.sort_values("date")
    .groupby("country")
    .tail(1)
)

gdp = (
    latest.sort_values("gdp", ascending=False)
)

plt.figure(figsize=(10,6))

plt.bar(
    gdp["country"],
    gdp["gdp"]
)

plt.xticks(rotation=45)

plt.title("GDP by Country")

plt.tight_layout()

plt.savefig("visuals/gdp_by_country.png")

plt.close()


life = (
    latest.sort_values(
        "life_expectancy",
        ascending=False
    )
)

plt.figure(figsize=(10,6))

plt.bar(
    life["country"],
    life["life_expectancy"]
)

plt.xticks(rotation=45)

plt.title("Life Expectancy")

plt.tight_layout()

plt.savefig("visuals/life_expectancy.png")

plt.close()


population = (
    latest.sort_values(
        "population",
        ascending=False
    )
)

plt.figure(figsize=(10,6))

plt.bar(
    population["country"],
    population["population"]
)

plt.xticks(rotation=45)

plt.title("Population")

plt.tight_layout()

plt.savefig("visuals/population.png")

plt.close()

print("EDA Completed")
