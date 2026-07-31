
import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="Nutrition IA 🥗", page_icon="🥗")

st.title("🥗 Nutrition IA Pro")
st.write("Prends ton repas en photo et laisse l'IA analyser ton assiette !")
st.write("---")

# Récupération de la clé API
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
else:
    st.error("⚠️ La clé API 'GEMINI_API_KEY' n'est pas configurée dans Streamlit Secrets.")
    st.stop()

# Bouton photo
photo = st.camera_input("Prends ton assiette en photo 📸")

if photo:
    img = Image.open(photo)
    st.image(img, caption="Ton repas à analyser", use_column_width=True)
    
    if st.button("🔍 Analyser l'assiette avec l'IA"):
        with st.spinner("Analyse de la valeur nutritionnelle en cours..."):
            try:
                prompt = """
                Tu es un expert en nutrition compétent, motivant et bienveillant.
                Analyse l'image de ce plat et fournis les détails suivants :
                1. 🍲 **Nom du plat / Aliments identifiés**
                2. 📊 **Estimation nutritionnelle globale** (Calories approximatives, Protéines, Glucides, Lipides)
                3. ✅ **Points forts** pour la santé
                4. 💡 **Conseils / Ajustements** pour rendre ce repas encore plus équilibré
                5. ⭐ **Note globale sur 10** pour la qualité nutritionnelle de cette assiette
                """
                
                response = client.models.generate_content(
                    model="gemini-2,0-flash",
                
                    contents=[prompt, img]
                )
                
                st.success("Analyse terminée !")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Une erreur est survenue lors de l'analyse : {e}")
                
