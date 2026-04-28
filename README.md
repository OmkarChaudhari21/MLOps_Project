# ChurnGuard AI: End-to-End MLOps for Customer Churn Prediction

**Author:** Omkar Ashok Chaudhari  
**Roll Number:** NA22B059  

---

## Overview

ChurnGuard AI is a production-ready MLOps system designed to predict customer churn in telecom/subscription-based businesses. The system enables companies to proactively identify at-risk customers and take targeted retention actions. 

This project implements a complete machine learning lifecycle, from data ingestion to deployment and monitoring.

## Problem Statement

Companies face difficulty in identifying customers who are likely to leave their services. Losing customers leads to revenue loss and increased costs for acquiring new users. This project aims to predict customer churn in advance so that companies can take actions to retain high-risk customers.

## Key Features

* **Predictive Analytics:** Calculate churn probability for each customer.
* **Risk Classification:** Categorize customers into **Low Risk**, **Medium Risk**, and **High Risk**.
* **Explainability:** Provide SHAP-based feature importance for predictions.
* **Production Deployment:** Expose a REST API for real-time predictions.
* **System Observability:** Monitor system and API metrics using Prometheus.
* **Reproducibility:** Maintain an end-to-end reproducible MLOps pipeline using MLflow and Docker.

---

## Tech Stack

| Component | Technology |
| :--- | :--- |
| **ML Model** | XGBoost, Logistic Regression, Random Forest |
| **Backend API** | FastAPI |
| **Frontend** | Streamlit |
| **Experiment Tracking** | MLflow |
| **Monitoring** | Prometheus with Grafana |
| **Version Control** | DVC |
| **Containerization** | Docker, Docker Compose |
| **Language** | Python |

---

## Dataset

**Telco Customer Churn Dataset (Kaggle)**
* Customer demographics
* Service usage
* Billing details
* Churn labels

---

## System Architecture & Pipeline

### ML Pipeline Flow
Data Ingestion -> Data Validation -> Preprocessing -> Feature Engineering -> Model Training -> Evaluation -> Deployment

### Feature Engineering
* Tenure groups
* Charge ratio features
* Encoded categorical variables

### Production Architecture
User (Streamlit UI) -> FastAPI (/predict API) -> Trained ML Model (XGBoost) -> Prediction + SHAP Explanation -> Logging + Monitoring (Prometheus)

---

## API Endpoints

| Endpoint | Description |
| :--- | :--- |
| `/predict` | Predict churn risk based on user payload |
| `/health` | Service health check |
| `/ready` | Readiness check |
| `/metrics` | Prometheus metrics |

---

## Application Components

**Frontend (Streamlit)**
* User-friendly dashboard displaying churn probability and risk category.
* Visualizes SHAP-based feature importance and business insights.

**Monitoring (Prometheus)**
* Tracks API request count and endpoint usage to enable system observability.

**Feedback Loop**
* Logs predictions alongside actual outcomes for future analysis.
* Detects data drift and supports manual retraining triggers.

The pipeline follows a DAG-based orchestration design and can be directly integrated with Airflow. The current orchestrator.py simulates task-based execution similar to Airflow DAGs.

---

## Project Structure
```bash

├── api/                  # FastAPI backend
├── frontend/             # Streamlit UI
├── src/                  # ML pipeline code
├── data/                 # Raw & processed data
├── models/               # Saved models
├── mlruns/               # MLflow tracking
├── tests/                # Test cases
├── docs/                 # Documentation
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.frontend
├── prometheus.yml
├── requirements.txt
├── README.md
```

## Setup & Run

### Clone Repository
```bash
git clone https://github.com/OmkarChaudhari21/MLOps_Project
cd MLOps_Project
```
### Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run ML Pipeline
```bash
python -m src.orchestrator
```
### Start System (Docker)
```bash
docker compose up --build -d
```

---

## Access Application

| Service     | URL                      |
|------------|--------------------------|
| Frontend   | http://localhost:8501    |
| API Docs   | http://localhost:8000/docs |
| Prometheus | http://localhost:9090    |
| Grafana    | http://localhost:3001    |

---

## Testing
```bash
pytest tests/
```

## Results

- ROC-AUC: approximately 0.85  
- Accuracy: approximately 80%  
- Provides reliable churn prediction with explainability  

---

## Limitations and Future Work

- Automated retraining not implemented  
- Alerting system not integrated  
- Model registry (MLflow stages) can be improved  
- Grafana dashboard not included  

---

## Future Improvements

- Integrate Airflow for orchestration  
- Add real-time data pipeline  
- Deploy on cloud platforms (AWS/GCP)  
- Implement automated retraining  
- Add alerting using Prometheus Alertmanager  

---

## Conclusion

This project demonstrates a complete MLOps pipeline that bridges machine learning and production systems. It ensures scalability, reproducibility, and real-time decision support for customer retention.
