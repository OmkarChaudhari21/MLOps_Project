import os
import pandas as pd
import joblib
import mlflow
import shap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from xgboost import XGBClassifier
from src.logger import logger

def train():
    logger.info("Starting Model Training...")
    df = pd.read_csv("data/processed/features.csv")
    
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    num_features = ["tenure", "MonthlyCharges", "TotalCharges", "ChargeRatio"]
    cat_features = ["Contract", "InternetService", "TenureGroup"]
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
        ]
    )
    
    model = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=42)
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", model)])
    
    mlflow.set_experiment("Telco_Churn_Pipeline")
    with mlflow.start_run():
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        y_prob = pipeline.predict_proba(X_test)[:, 1]
        
        acc, prec = accuracy_score(y_test, y_pred), precision_score(y_test, y_pred)
        rec, auc = recall_score(y_test, y_pred), roc_auc_score(y_test, y_prob)
        
        mlflow.log_params({"n_estimators": 100, "max_depth": 4})
        mlflow.log_metrics({"accuracy": acc, "precision": prec, "recall": rec, "roc_auc": auc})
        mlflow.sklearn.log_model(pipeline, "model")
        
        logger.info(f"Model trained. AUC: {auc:.4f}, Accuracy: {acc:.4f}")
        
        os.makedirs("models", exist_ok=True)
        joblib.dump(pipeline, "models/model.pkl")
        
        # Fit SHAP explainer on preprocessed training data
        X_train_transformed = preprocessor.fit_transform(X_train)
        # Handle sparse matrix from OneHotEncoder
        if hasattr(X_train_transformed, "toarray"):
            X_train_transformed = X_train_transformed.toarray()
            
        explainer = shap.TreeExplainer(model)
        joblib.dump(explainer, "models/explainer.pkl")
        
        # Save feature names for SHAP
        cat_names = preprocessor.named_transformers_['cat'].get_feature_names_out(cat_features)
        feature_names = num_features + list(cat_names)
        joblib.dump(feature_names, "models/feature_names.pkl")
        
    logger.info("Model and Explainer saved to /models.")