# User Manual
1. **Data Scientists**: Run `python src/orchestrator.py` to retrain. View artifacts in `/models`.
2. **DevOps**: Use `docker-compose up -d` to deploy. Check `localhost:9090` for Prometheus.
3. **Business Users**: Navigate to `localhost:8501`. Enter customer details, click "Predict", and read the Action Plan and SHAP drivers.