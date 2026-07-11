import joblib
import pandas as pd

model = joblib.load(
    "models/worldbank_model.pkl"
)

sample = pd.DataFrame(
    {
        "population": [21000000],
        "inflation": [9.4],
        "poverty": [58],
        "unemployment": [12],
        "life_expectancy": [64],
        "literacy": [88]
    }
)

prediction = model.predict(sample)

print()

print("Predicted GDP")

print(prediction[0])

prediction_df = sample.copy()

prediction_df["predicted_gdp"] = prediction

prediction_df.to_csv(
    "predictions/predictions.csv",
    index=False
)

print("Predictions Saved")
