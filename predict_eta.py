import xgboost as xgb
import pandas as pd

def predict_eta(distance_km, cargo_weight, weather_score):
    model = xgb.XGBRegressor()
    model.load_model("eta_model.json")
    input_df = pd.DataFrame([[distance_km, cargo_weight, weather_score]],
                            columns=["distance_km", "cargo_weight", "weather_score"])
    prediction = model.predict(input_df)
    return prediction[0]
