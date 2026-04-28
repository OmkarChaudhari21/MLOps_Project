from src.logger import logger

def validate_data(df):
    logger.info("Validating Data Schema...")
    expected_cols = ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Contract", "InternetService", "Churn"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected column: {col}")
    
    missing_pct = df.isnull().mean().max()
    if missing_pct > 0.1:
        logger.warning(f"High missing values detected: {missing_pct*100:.2f}%")
        
    logger.info("Data validation passed.")
    return True