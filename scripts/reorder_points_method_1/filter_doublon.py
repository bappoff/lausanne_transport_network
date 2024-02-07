import pandas as pd
import sys

# Recuperer le nom du fichier passe en argument
nom_fichier = sys.argv[1]  # Le premier argument est le nom du script, le second est votre argument

# Utiliser nom_fichier pour charger le fichier CSV correspondant
file_path = f'/Chemin/vers/le/fichier/enregistre/apres/execution/de/delete_col.py/{nom_fichier}_step1.csv'
# Continuer le reste du script en utilisant chemin_fichier_csv

data = pd.read_csv(file_path)

# Grouper les donnees par coordonnees et conserver la ligne avec le vertex_index le plus bas
data = data.sort_values('vertex_ind').drop_duplicates(subset=['lat', 'long'])

# Renumeroter les vertex_index pour qu'ils se suivent de maniere sequentielle
data = data.reset_index(drop=True)
data['vertex_ind'] = data.index

# Sauvegarder les modifications
new_file_path = f'/Chemin/vers/le/nouveau/fichier/csv/{nom_fichier}_step2.csv'  
data.to_csv(new_file_path, index=False)
