import streamlit as st
import requests
import pandas as pd

# API URL (Docker service name)
API_URL = "http://api:8000"

# Page config
st.set_page_config(page_title="ChurnGuard AI", layout="wide")

#  HEADER 
st.markdown("""
# 🔮 ChurnGuard AI
### Proactive Customer Retention System
---
""")

#  SIDEBAR 
with st.sidebar:
    st.header("📡 System Status")
    try:
        res = requests.get(f"{API_URL}/ready", timeout=2)
        if res.status_code == 200:
            st.success("API Ready")
        else:
            st.error("API Not Ready")
    except:
        st.error("API Unreachable")

    st.markdown("---")
    st.markdown("Built with:")
    st.markdown("- FastAPI")
    st.markdown("- XGBoost")
    st.markdown("- MLflow")
    st.markdown("- Docker")

#  INPUT SECTION 
st.subheader("📥 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (months)", 0, 100, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 900.0)

with col2:
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])

#  PREDICT BUTTON 
if st.button("🚀 Predict Churn Risk", use_container_width=True):

    payload = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": contract,
        "InternetService": internet
    }

    with st.spinner("Analyzing customer behavior..."):
        try:
            response = requests.post(f"{API_URL}/predict", json=payload)
            response.raise_for_status()
            data = response.json()

            prob = data['churn_probability'] * 100
            risk = data['risk_category']
            insight = data['actionable_insight']

            st.markdown("---")
            st.subheader("📊 Prediction Results")

            #  KPI CARDS 
            k1, k2, k3 = st.columns(3)

            k1.metric("Churn Probability", f"{prob:.2f}%")

            if risk == "Low":
                k2.success(f"🟢 {risk}")
            elif risk == "Medium":
                k2.warning(f"🟡 {risk}")
            else:
                k2.error(f"🔴 {risk}")

            k3.info(f"💡 {insight}")

            #  SHAP VISUALIZATION 
            st.markdown("---")
            st.subheader("📈 Top Drivers (SHAP)")

            drivers = data['top_churn_drivers_shap']

            if "error" not in drivers:
                df = pd.DataFrame(drivers.items(), columns=["Feature", "Impact"])
                df = df.sort_values(by="Impact", key=abs)

                st.bar_chart(df.set_index("Feature"))

                for feature, impact in drivers.items():
                    direction = "⬆️ Increases Risk" if impact > 0 else "⬇️ Decreases Risk"
                    st.write(f"**{feature}**: {direction} (Impact: {abs(impact):.3f})")
            else:
                st.warning("SHAP explanation unavailable.")

            #  INSIGHT BOX 
            st.markdown("---")
            if risk == "High":
                st.error("⚠️ High churn risk detected. Recommend offering discounts or proactive engagement.")
            elif risk == "Medium":
                st.warning("⚠️ Moderate churn risk. Monitor customer activity and engagement.")
            else:
                st.success("✅ Low churn risk. Maintain current engagement strategies.")

        except Exception as e:
            st.error(f"Prediction failed: {e}")

#  FOOTER 
st.markdown("""
---
<center>🚀 Built using MLOps | FastAPI | Streamlit | Docker</center>
""", unsafe_allow_html=True)