import streamlit as st
from data import predict_churn

st.set_page_config(page_title="Prediksi Churn Pelanggan", layout="centered")
st.title('📉 Prediksi Pelanggan yang Mengalami Churn')
st.write("Aplikasi ini memprediksi apakah pelanggan akan mengalami churn berdasarkan input dari pengguna.")

st.header('🧾 Masukkan Data Pelanggan')

data = {
    'age': st.number_input('Umur', min_value=18, max_value=100, value=25),
    'marital_status': st.selectbox('Status Pernikahan', ['Married', 'Single']),
    'Recency': st.number_input('Recency (hari sejak transaksi terakhir)', min_value=0),
    'Monetary': st.number_input('Monetary (total pembelian)', min_value=0),
    'Frequency': st.number_input('Frequency (jumlah transaksi)', min_value=0),
}

if st.button('Prediksi Churn'):
    try:
        prediction, probability = predict_churn(data)
        st.header('📍 Hasil Prediksi')

        if prediction == 1:
            st.success('✅ Pelanggan Mengalami Churn')
        else:
            st.info('❎ Pelanggan Tidak Mengalami Churn')

        st.write(f"🔢 Probabilitas Churn: **{probability:.2%}**")

    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan saat melakukan prediksi: {e}")

st.markdown("---")
st.write("Aplikasi ini dibuat untuk membantu memprediksi churn pelanggan.")
