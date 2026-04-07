import streamlit as st
from PIL import Image
import numpy as np


st.title("Klasifikasi Kucing vs Anjing")

file = st.file_uploader("Upload gambar", type=["jpg","png","jpeg"])

if file:
    img = Image.open(file).resize((150,150))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)

    if pred[0][0] > 0.5:
        st.success("🐶 Ini adalah ANJING (Label: 1)")
    else:
        st.success("🐱 Ini adalah KUCING (Label: 0)")
