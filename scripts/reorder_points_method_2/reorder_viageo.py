import pandas as pd
import numpy as np
import sys
from geopy.distance import geodesic
import time

start_time = time.time()

# Fonction pour calculer la distance entre deux points
def calculer_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).meters

def run_script(nom_fichier, premier_point):
    print(nom_fichier)
    # Charger les donnees
    data = pd.read_csv(f'/Users/baptiste/Desktop/osm2qgis/csv/after/{nom_fichier}.csv')

    colonnes_a_supprimer = ['other_tags', 'distance', 'angle', 'WKT', 'WKT.1', 'Nouvel_Ord','ordre']
    # Boucle sur la liste des colonnes et suppression si elles existent
    for col in colonnes_a_supprimer:
        if col in data.columns:
            data.drop(col, axis=1, inplace=True)

    # Grouper les donnees par coordonnees et conserver la ligne avec le vertex_index le plus bas
    data = data.sort_values('vertex_ind').drop_duplicates(subset=['lat', 'long'])

    # Renumeroter les vertex_index pour qu'ils se suivent de maniere sequentielle
    #data = data.reset_index(drop=True)
    #data['vertex_ind'] = data.index

    # Initialiser la colonne pour le nouvel ordre
    data['Nouvel_Ordre'] = np.nan
    indice_point_depart = data[data['vertex_ind'] == premier_point].index[0]
    data.at[indice_point_depart, 'Nouvel_Ordre'] = 0

    # Boucle pour numeroter les points
    for i in range(1, len(data)):
        print('Recherche du point le plus proche...')
        # Point actuel
        point_actuel = data.loc[data['Nouvel_Ordre'] == i - 1, ['lat', 'long']].iloc[0]

        # Calculer les distances par rapport au point actuel pour les points non numerotes
        distances = data.loc[data['Nouvel_Ordre'].isna()].apply(
            lambda row: calculer_distance(row['lat'], row['long'], point_actuel['lat'], point_actuel['long']), 
            axis=1
        )

        # Trouver l'indice du point le plus proche
        prochain_point_indice = distances.idxmin()
        data.at[prochain_point_indice, 'Nouvel_Ordre'] = i
        #print(i+1, 'point numerotes sur', len(data))

    data = data.sort_values(by='Nouvel_Ordre')

    # Sauvegarder les resultats
    data.to_csv(f'/Users/baptiste/Desktop/osm2qgis/csv/after/{nom_fichier}_final.csv', index=False)



# Lire le fichier avec les noms des fichiers a traiter
fichiers_df = pd.read_csv('/Users/baptiste/Desktop/osm2qgis/csv/csv_to_traiter/lines_to_reorder.csv')
#print(fichiers_df)

# Iterer sur chaque nom de fichier et executer les scripts
for _, row in fichiers_df.iterrows():
    run_script(row['nom_fichier'], row['premier_point'])



end_time = time.time()

# Calcul de la duree totale
total_time_seconds = end_time - start_time

# Conversion en heures, minutes et secondes
hours = total_time_seconds // 3600
minutes = (total_time_seconds % 3600) // 60
seconds = total_time_seconds % 60

# Affichage du temps d'execution
print(f"Temps d'execution: {int(hours)} heures, {int(minutes)} minutes et {seconds:.2f} secondes")
