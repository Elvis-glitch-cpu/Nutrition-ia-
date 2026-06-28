
import streamlit as st

st.set_page_config(page_title="Nutrition IA 🥑", page_icon="🥗", layout="centered")

st.title("🥗 Nutrition IA Pro")
st.write("Prends ton repas en photo et laisse l'IA analyser ton assiette !")
st.write("---")

# Bouton magique qui ouvre l'appareil photo du téléphone
photo = st.camera_input("Prends ton assiette en photo 📸")

if photo:
    st.image(photo, caption="Ton repas à analyser")
    st.success("Image bien reçue ! Prochaine étape : Connexion à l'IA...")
