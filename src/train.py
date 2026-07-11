import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib

df = pd.read_csv(
    "data/cleaned/worldbank_features.csv"
)

df = df.dropna()

features = [
    "population",
    "inflation",
    "poverty",
    "unemployment",
    "life_expectancy",
    "literacy"
]

X = df[features]

y = df["gdp"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print("MAE:", mean_absolute_error(y_test, predictions))

print("MSE:", mean_squared_error(y_test, predictions))

print("R2:", r2_score(y_test, predictions))

joblib.dump(
    model,
    "models/worldbank_model.pkl"
)

print("Model Saved")
