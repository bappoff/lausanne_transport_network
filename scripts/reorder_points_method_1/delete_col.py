import pandas as pd
import sys

# Recuperer le nom du fichier passe en argument
nom_fichier = sys.argv[1]  # Le premier argument est le nom du script, le second est votre argument

# Utiliser nom_fichier pour charger le fichier CSV correspondant
file_path = f'/Chemin/vers/le/fichier/contenant/les/noms/des/fichiers/csv/{nom_fichier}.csv'
# Continuer le reste du script en utilisant chemin_fichier_csv

# Chemin vers le nouveau fichier CSV
new_file_path = f'/Chemin/vers/le/nouveau/fichier/csv/{nom_fichier}_step1.csv'

# Charger les donnees depuis le fichier CSV
data = pd.read_csv(file_path)

colonnes_a_supprimer = ['other_tags', 'distance', 'angle', 'WKT']

# Boucle sur la liste des colonnes et suppression si elles existent
for col in colonnes_a_supprimer:
    if col in data.columns:
        data.drop(col, axis=1, inplace=True)

# Sauvegarder le DataFrame modifie dans le nouveau fichier
data.to_csv(new_file_path, index=False)
