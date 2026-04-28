from src.data_ingestion import ingest_data
from src.data_validation import validate_data
from src.preprocessing import preprocess_data
from src.feature_engineering import engineer_features
from src.train_model import train
from src.drift_detection import detect_drift
from src.logger import logger
import os

def run_pipeline():
    logger.info("=== STARTING ML PIPELINE DAG ===")
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    # 1. Ingestion
    raw_df = ingest_data()
    # 2. Validation
    validate_data(raw_df)
    # 3. Preprocessing
    clean_df = preprocess_data(raw_df)
    # 4. Feature Engineering
    features_df = engineer_features(clean_df)
    # 5. Training
    train()
    # 6. Drift Monitoring
    detect_drift()
    logger.info("=== PIPELINE COMPLETION SUCCESS ===")

if __name__ == "__main__":
    run_pipeline()