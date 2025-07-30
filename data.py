# data.py
import pandas as pd
import joblib

# Load model churn
try:
    model = joblib.load('logistic_regression_model_pemograman1.pkl')
except FileNotFoundError:
    raise FileNotFoundError("❌ File model tidak ditemukan. Pastikan file .pkl tersedia.")

# Fungsi untuk memprediksi churn pelanggan
def predict_churn(data: dict):
    input_df = pd.DataFrame([{
        "age": data['age'],
        "marital_status": 1 if data['marital_status'] == "Married" else 0,
        "Recency": data['Recency'],
        "Frequency": data['Frequency'],
        "Monetary": data['Monetary'],
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability
