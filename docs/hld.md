# High-Level Design (HLD)
1. **Data Engineering Layer**: Python scripts execute ingestion, validation, preprocessing, and feature engineering.
2. **Model Training Layer**: XGBoost model trained via Scikit-Learn pipeline. Tracked using MLflow.
3. **Serving Layer**: FastAPI exposes REST endpoints. SHAP integration provides interpretability.
4. **Monitoring Layer**: Prometheus scrapes API metrics. Logs record predictions for drift detection.
5. **Presentation Layer**: Streamlit app for business stakeholders.