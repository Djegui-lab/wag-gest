import os
import streamlit as st

# Définir le chemin relatif du fichier JSON
json_file_path = "courtier-devis-automatique-e47e170f58f7.json"

# Vérifiez si le fichier existe
if not os.path.exists(json_file_path):
    st.error(f"Le fichier JSON à l'emplacement {json_file_path} est introuvable.")
else:
    st.success(f"Le fichier JSON a été trouvé à l'emplacement : {json_file_path}")
