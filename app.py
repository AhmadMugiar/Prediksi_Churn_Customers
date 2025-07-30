# app.py
import streamlit as st
from data import predict_churn

st.set_page_config(page_title="Prediksi Churn", layout="centered")
st.title("📉 Prediksi Churn Pelanggan Retail")
st.write("Masukkan data pelanggan untuk mengetahui apakah pelanggan berisiko churn.")

st.header("🧾 Form Input Pelanggan")

# Ambil input dari user
data = {
    'age': st.number_input('Umur', min_value=18, max_value=100, value=30),
    'marital_status': st.selectbox('Status Pernikahan', ['Married', 'Single']),
    'Recency': st.number_input('Recency (hari sejak transaksi terakhir)', min_value=0),
    'Monetary': st.number_input('Monetary (total pembelian)', min_value=0),
    'Frequency': st.number_input('Frequency (jumlah transaksi)', min_value=0),
}

# Tombol prediksi
if st.button("🔍 Prediksi Churn"):
    try:
        prediction, probability = predict_churn(data)

        st.subheader("📍 Hasil Prediksi")
        if prediction == 1:
            st.error("⚠️ Pelanggan diprediksi mengalami churn.")
        else:
            st.success("✅ Pelanggan diprediksi tidak mengalami churn.")

        st.write(f"Probabilitas churn: **{probability:.2%}**")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
