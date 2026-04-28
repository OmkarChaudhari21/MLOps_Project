import pandas as pd
from src.logger import logger

def preprocess_data(df):
    logger.info("Preprocessing Data...")
    df = df.copy()
    
    # Convert TotalCharges to numeric (IMPORTANT FIX)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Handle missing values
    df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'] * df['tenure'])
    
    # Encode target
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Drop ID column
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)
        
    logger.info("Preprocessing complete.")
    return df