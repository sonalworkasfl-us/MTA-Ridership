import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.model_predict import predict_with_model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PredictionRequest(BaseModel):
    month: int
    day: int
    hour: int
    borough: str
    payment_method: str


app = FastAPI(title="MTA Ridership Prediction API")

def load_model(model_name: str):
    model_path = os.path.join(BASE_DIR, "models", f"{model_name}_tuned.pkl")
    return joblib.load(model_path)

@app.post("/predict/{model_name}")
def predict(model_name: str, request: PredictionRequest):
    # Convert request to DataFrame
    new_data = pd.DataFrame([request.dict()])

    prediction = predict_with_model(model_name, new_data)

    return {"model": model_name, "prediction": float(prediction[0])}
