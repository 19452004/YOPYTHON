import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_mobil.sav', 'rb'))

st.title("Selamat datang diaplikasi estimasi harga mobil")
st.title("Estimasi harga mobil bekas")

year = st.number_input("Input tahun mobil")
mileage = st.number_input("Input jarak temput mobil(mil)")
tax = st.number_input("Input pajak mobil")
mpg = st.number_input("Input konsumsi BBM")
engineSize = st.number_input("Input Ukuran Mesin")

#indetifikasi model prediksi 
predict = ''

if st.button("Estimasi harga"):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write ("Estimasi harga mobil bekas dalam IDR(Juta): ", predict * 19000)