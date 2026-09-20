from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("fuel_model.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()


class FuelRequest(BaseModel):
    Distance_km: float
    Vehicle_Type: str
    Passengers: int
    Nominal_L_per_100km: float
    Duration_min: float


@app.get("/")
def home():
    return {"message": "Fuel Prediction API is running"}


@app.post("/predict")
def predict(data: FuelRequest):

    # One-hot encoding for Vehicle_Type
    vehicle_types = ["Bus", "SUV", "Sedan", "Van"]

    vehicle_encoded = {
        f"Vehicle_Type_{vehicle}": 1 if data.Vehicle_Type == vehicle else 0
        for vehicle in vehicle_types
    }

    # Features in the EXACT same order used during training
    features = pd.DataFrame([{
        "Distance_km": data.Distance_km,
        "Passengers": data.Passengers,
        "Nominal_L_per_100km": data.Nominal_L_per_100km,
        "Duration_min": data.Duration_min,
        "Vehicle_Type_Bus": vehicle_encoded["Vehicle_Type_Bus"],
        "Vehicle_Type_SUV": vehicle_encoded["Vehicle_Type_SUV"],
        "Vehicle_Type_Sedan": vehicle_encoded["Vehicle_Type_Sedan"],
        "Vehicle_Type_Van": vehicle_encoded["Vehicle_Type_Van"],
    }])

    # Scale numeric features
    numeric_columns = [
        "Distance_km",
        "Passengers",
        "Nominal_L_per_100km",
        "Duration_min"
    ]

    features[numeric_columns] = scaler.transform(
        features[numeric_columns]
    )

    # Prediction
    prediction = model.predict(features)

    return {
        "predicted_fuel": float(prediction[0])
    }