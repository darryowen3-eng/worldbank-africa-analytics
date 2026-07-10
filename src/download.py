import wbdata
import pandas as pd

indicators = {
    "NY.GDP.MKTP.CD": "gdp",
    "SP.POP.TOTL": "population",
    "FP.CPI.TOTL.ZG": "inflation",
    "SI.POV.DDAY": "poverty",
    "SL.UEM.TOTL.ZS": "unemployment",
    "SP.DYN.LE00.IN": "life_expectancy",
    "SE.ADT.LITR.ZS": "literacy"
}

countries = [
    "ZMB",
    "KEN",
    "TZA",
    "UGA",
    "RWA",
    "ZAF",
    "BWA",
    "NAM"
]

df = wbdata.get_dataframe(
    indicators,
    country=countries
)

df.reset_index(inplace=True)

df.to_csv(
    "data/raw/worldbank_africa.csv",
    index=False
)

print(df.head())
