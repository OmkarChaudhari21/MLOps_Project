import pandas as pd
from src.logger import logger

def engineer_features(df):
    logger.info("Engineering Features...")
    df = df.copy()
    
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[-1, 12, 24, 48, 60, 100],
        labels=['0-1Y', '1-2Y', '2-4Y', '4-5Y', '5Y+']
    ).astype(str)

    df['ChargeRatio'] = df['TotalCharges'] / (df['MonthlyCharges'] + 1e-5)

    logger.info("Feature engineering complete.")
    df.to_csv("data/processed/features.csv", index=False)
    return df