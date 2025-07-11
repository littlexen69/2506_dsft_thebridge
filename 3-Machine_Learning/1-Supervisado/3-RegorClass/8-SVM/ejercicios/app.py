import streamlit as st
import pickle

st.title('Mi modelo')

with open("final_model.pkl", "rb") as entrada:
    modelo = pickle.load(entrada)

x1 = st.slider("Introducir variable x1", 0, 10)

x2 = st.slider("Introducir variable x2", 0, 10)

if st.button("Predecir con modelo"):
    st.metric("Que dice el modelo?", modelo.predict_proba([[x1,x2]])[:,1], +1.7)