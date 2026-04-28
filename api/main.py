from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os
import shap
from prometheus_fastapi_instrumentator import Instrumentator
import logging

logging.basicConfig(filename="data/api_predictions.log", level=logging.INFO)

app = FastAPI(title="Telco Churn API", description="Predicts churn risk and provides SHAP explanations.")
Instrumentator().instrument(app).expose(app)

# Load artifacts
try:
    pipeline = joblib.load("models/model.pkl")
    explainer = joblib.load("models/explainer.pkl")
    feature_names = joblib.load("models/feature_names.pkl")
except Exception:
    pipeline, explainer, feature_names = None, None, None

class CustomerInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str

@app.get("/health")
def health(): return {"status": "healthy"}

@app.get("/ready")
def ready():
    if pipeline: return {"status": "ready"}
    raise HTTPException(status_code=503, detail="Model artifacts missing. Run pipeline first.")

@app.post("/predict")
def predict(data: CustomerInput):
    if not pipeline:
        raise HTTPException(status_code=503, detail="Model not loaded.")
        
    # Reconstruct dictionary and apply engineer features logic manually for inference
    input_dict = data.model_dump()
    
    # Feature Engineering (mimic src/feature_engineering.py)
    tenure_bins = [-1, 12, 24, 48, 60, 100]
    labels = ['0-1Y', '1-2Y', '2-4Y', '4-5Y', '5Y+']
    tenure_grp = labels[np.digitize(input_dict['tenure'], tenure_bins) - 1]
    charge_ratio = input_dict['TotalCharges'] / (input_dict['MonthlyCharges'] + 1e-5)
    
    df = pd.DataFrame([{
        "tenure": input_dict['tenure'],
        "MonthlyCharges": input_dict['MonthlyCharges'],
        "TotalCharges": input_dict['TotalCharges'],
        "Contract": input_dict['Contract'],
        "InternetService": input_dict['InternetService'],
        "TenureGroup": tenure_grp,
        "ChargeRatio": charge_ratio
    }])

    # Predict
    prob = pipeline.predict_proba(df)[0][1]
    
    # Risk calculation
    risk = "Low" if prob < 0.4 else "Medium" if prob < 0.7 else "High"
    insight = "Offer heavy retention discount" if risk == "High" else "Monitor usage" if risk == "Medium" else "Maintain engagement"

    # SHAP Explanations
    try:
        preprocessor = pipeline.named_steps['preprocessor']
        model = pipeline.named_steps['classifier']
        
        X_trans = preprocessor.transform(df)
        if hasattr(X_trans, "toarray"): X_trans = X_trans.toarray()
        
        shap_values = explainer.shap_values(X_trans)[0]
        
        # Get top 3 features driving this specific prediction
        shap_dict = dict(zip(feature_names, shap_values))
        top_features = sorted(shap_dict.items(), key=lambda x: abs(x[1]), reverse=True)[:3]
        drivers = {k: float(v) for k, v in top_features}
    except Exception as e:
        drivers = {"error": "SHAP explanation failed"}

    # Logging for monitoring
    logging.info(f"Input: {input_dict} | Prob: {prob} | Risk: {risk}")

    return {
        "churn_probability": float(prob),
        "risk_category": risk,
        "actionable_insight": insight,
        "top_churn_drivers_shap": drivers
    }