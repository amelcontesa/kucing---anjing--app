import streamlit as st

st.title("Aplikasi Klasifikasi Kucing vs Anjing 🐱🐶")

uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang diupload", use_column_width=True)
    
    st.write("### Hasil Prediksi:")
    st.success("Ini contoh hasil (dummy): Kucing 🐱")
