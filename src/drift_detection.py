import pandas as pd
import numpy as np
from src.logger import logger

def detect_drift():
    """Simple Data Drift Detection comparing Training vs current 'Production' requests"""
    logger.info("Checking for Data Drift...")
    try:
        # Load training baseline
        train_df = pd.read_csv("data/processed/features.csv")
        train_mean = train_df["MonthlyCharges"].mean()
        
        # In a real scenario, this loads from an API logs database.
        # Simulating recent predictions log:
        prod_mean = train_mean * 1.15 # Simulated drift
        
        drift_threshold = 0.1 # 10% shift
        shift = abs(prod_mean - train_mean) / train_mean
        
        if shift > drift_threshold:
            logger.warning(f"DATA DRIFT DETECTED! MonthlyCharges shifted by {shift*100:.2f}%. Retraining recommended.")
        else:
            logger.info("No significant data drift detected.")
    except Exception as e:
        logger.error(f"Drift detection error: {e}")