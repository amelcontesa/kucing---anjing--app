import streamlit as st
from PIL import Image
import numpy as np

st.title("Aplikasi Klasifikasi Kucing vs Anjing 🐱🐶")

uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diupload", use_column_width=True)
    
    # simulasi prediksi sederhana
    img_array = np.array(image)
    rata_rata = img_array.mean()
    
    st.write("### Hasil Prediksi:")
    
    if rata_rata > 120:
        st.success("Prediksi: Anjing 🐶")
    else:
        st.success("Prediksi: Kucing 🐱")
