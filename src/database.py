import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://analyst:analytics123@localhost/worldbank"
)

df = pd.read_csv(
    "data/cleaned/worldbank_features.csv"
)

df.to_sql(
    "worldbank_data",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully")
