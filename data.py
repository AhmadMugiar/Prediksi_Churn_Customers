import pandas as pd
import joblib

# Load model
try:
    model = joblib.load('logistic_regression_model_pemograman1.pkl')
except FileNotFoundError:
    raise FileNotFoundError("Model file tidak ditemukan.")

# Fungsi prediksi churn
def predict_churn(data: dict):
    input_df = pd.DataFrame([{
        "age": data['age'],
        "marital_status": 1 if data['marital_status'] == "Married" else 0,
        "Recency": data['Recency'],
        "Frequency": data['Frequency'],
        "Monetary": data['Monetary'],
    }])

    input_df = input_df[['age', 'marital_status', 'Recency', 'Frequency', 'Monetary']]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability
