# User Manual: ChurnGuard AI

## Introduction

ChurnGuard AI is a web-based application that predicts customer churn risk using machine learning. It provides:

- Churn probability
- Risk classification (Low / Medium / High)
- Actionable insights
- Feature-level explanations (SHAP)

This manual guides users on how to operate the system.

---

## Accessing the Application

Make sure the system is running, then open:

- Frontend (UI): http://localhost:8501  
- API Docs: http://localhost:8000/docs  
- Monitoring (Prometheus): http://localhost:9090  
- Dashboard (Grafana): http://localhost:3001  

---

## Using the Web Interface (Streamlit UI)

### Step 1: Open the Application

Go to:
http://localhost:8501

---

### Step 2: Enter Customer Details

Fill in the required inputs:

- **Tenure (months)** → Duration of customer subscription  
- **Monthly Charges ($)** → Monthly billing amount  
- **Total Charges ($)** → Total billing so far  
- **Contract Type** → Month-to-month / One year / Two year  
- **Internet Service** → Fiber optic / DSL / No  

---

### Step 3: Click “Predict Churn Risk”

Click the button:
**Predict Churn Risk**

The system will process input and generate results.

---

### Step 4: View Results

You will see:

#### Churn Probability
- Example: 17.4%
- Indicates likelihood of churn

#### Risk Category
- Low → Safe customer  
- Medium → Monitor  
- High → Immediate action required  

#### Action Plan
- Suggested business action (e.g., offer discount)

---

### Step 5: Interpret SHAP Explanation

- Displays top contributing features
- Shows whether each feature:
  - Increased churn risk
  - Decreased churn risk

---

## Using the API (Advanced Users)

Go to:
http://localhost:8000/docs

### Endpoint: `/predict`

- Method: POST  
- Input: JSON payload  
- Output: churn probability + risk + explanation  

---

## Monitoring the System

### Prometheus

- URL: http://localhost:9090  
- Query example: http_requests_total


Tracks API usage and system metrics.

---

### Grafana Dashboard

- URL: http://localhost:3001  
- Visualizes real-time API metrics  
- Displays request trends and monitoring graphs  

---

## Error Handling

- If API is not reachable → check Docker containers  
- If prediction fails → verify input values  
- If UI not loading → restart frontend container  

---

## Restarting the System
docker compose down
docker compose up --build -d

## Notes
Model predictions are based on trained ML model (XGBoost)
Results are probabilistic, not deterministic
System supports real-time inference

---

## Support For issues:

Check logs in data/api_predictions.log
Verify Docker services are running

## Summary
ChurnGuard AI enables:

Real-time churn prediction
Business decision support
Explainable AI insights
Monitoring and observability