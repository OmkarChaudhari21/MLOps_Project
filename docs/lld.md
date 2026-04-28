# Low-Level Design (LLD) - API Specs
**Endpoint:** `POST /predict`
**Request Body:**
```json
{
  "tenure": 12, "MonthlyCharges": 75.0, "TotalCharges": 900.0, 
  "Contract": "Month-to-month", "InternetService": "Fiber optic"
}