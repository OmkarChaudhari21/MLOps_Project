import os
import pandas as pd
import numpy as np
from src.logger import logger

def ingest_data():
    logger.info("Starting Data Ingestion...")
    os.makedirs("data/raw", exist_ok=True)
    path = "data/raw/telco_churn.csv"
    
    if not os.path.exists(path):
        logger.info("Dataset not found. Generating synthetic Telco data.")
        np.random.seed(42)
        n = 2000
        df = pd.DataFrame({
            "customerID": [f"CUST_{i:04d}" for i in range(n)],
            "tenure": np.random.randint(0, 73, n),
            "MonthlyCharges": np.random.uniform(18.0, 120.0, n),
            "TotalCharges": np.random.uniform(18.0, 8000.0, n),
            "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n),
            "InternetService": np.random.choice(["DSL", "Fiber optic", "No"], n),
            "Churn": np.random.choice(["Yes", "No"], n, p=[0.26, 0.74])
        })
        # Introduce some missing values to test preprocessing
        df.loc[df.sample(frac=0.01).index, 'TotalCharges'] = np.nan
        df.to_csv(path, index=False)
    else:
        df = pd.read_csv(path)
    logger.info(f"Ingested {len(df)} records.")
    return df