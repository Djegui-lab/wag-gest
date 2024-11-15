import os

# Définir le chemin du fichier JSON directement
json_file_path = "C:\projet\courtier-devis-automatique-e47e170f58f7.json"

# Vérifiez si le fichier existe
if not os.path.exists(json_file_path):
    raise FileNotFoundError(f"Le fichier JSON à l'emplacement {json_file_path} est introuvable.")

print(f"Le fichier JSON a été trouvé à l'emplacement : {json_file_path}")
