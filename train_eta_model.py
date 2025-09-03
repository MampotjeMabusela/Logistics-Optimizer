import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

df = pd.read_csv("shipment_data.csv")
X = df[["distance_km", "cargo_weight", "weather_score"]]
y = df["eta_hours"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = xgb.XGBRegressor()
model.fit(X_train, y_train)
model.save_model("eta_model.json")
