# System Architecture Diagram
[Data Sources] -> [Data Pipeline (DAG/Python)] -> [MLflow Model Registry] -> [Joblib Artifacts]
                                                                                |
[User] <--> [Streamlit Frontend UI] <--> [FastAPI Model Serving] <---------------
                                                |
                                    [Prometheus Metrics / Drift Logs]