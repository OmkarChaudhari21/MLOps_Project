import streamlit as st
import os

st.title("ML Pipeline Dashboard")

st.markdown("### Pipeline Stages")

st.write("""
1. Data Ingestion  
2. Data Validation  
3. Preprocessing  
4. Feature Engineering  
5. Model Training  
6. Evaluation  
7. Deployment  
""")

st.markdown("### Pipeline Status")

if os.path.exists("models/model.pkl"):
    st.success("Model Trained & Available")
else:
    st.warning("Model not found")

st.markdown("### Logs")

try:
    with open("data/api_predictions.log", "r") as f:
        logs = f.readlines()[-10:]
        for log in logs:
            st.text(log.strip())
except:
    st.info("No logs available")

st.markdown("### MLflow UI")
st.write("http://localhost:5000")