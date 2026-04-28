from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_requires_model():
    # If pipeline hasn't run, this correctly tests the 503 fallback
    # If pipeline HAS run, it tests the 200 OK response.
    payload = {
        "tenure": 24,
        "MonthlyCharges": 80.0,
        "TotalCharges": 1920.0,
        "Contract": "Month-to-month",
        "InternetService": "Fiber optic"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code in [200, 503]
    
    if response.status_code == 200:
        data = response.json()
        assert "churn_probability" in data
        assert "risk_category" in data
        assert "actionable_insight" in data