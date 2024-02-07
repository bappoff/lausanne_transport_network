import pandas as pd
from geopy.distance import geodesic
import sys

# Recuperer le nom du fichier passe en argument
nom_fichier = sys.argv[1]  # Le premier argument est le nom du script, le second est votre argument

# Utiliser nom_fichier pour charger le fichier CSV correspondant
df = pd.read_csv(f'/Users/baptiste/Desktop/osm2qgis/csv/during/{nom_fichier}_step2.csv')


# Fonction pour calculer la distance entre deux points
def calculer_distance(row, next_row):
    if next_row is not None:
        return geodesic((row['lat'], row['long']), (next_row['lat'], next_row['long'])).meters
    else:
        return None

# Calcul de la distance pour chaque point
df['distance'] = [calculer_distance(df.iloc[i], df.iloc[i+1]) if i < len(df) - 1 else None for i in range(len(df))]

# Calcul de la distance_to_next_part
def distance_last_to_last(df):
    distances = [None] * len(df)
    unique_parts = df['vertex_par'].unique()

    for part in unique_parts[:-1]:
        last_of_current = df[df['vertex_par'] == part].iloc[-1]
        #next_part_df = df[df['vertex_par'] == part + 1]

        part_index = list(unique_parts).index(part)
        next_part = unique_parts[part_index + 1]
        next_part_df = df[df['vertex_par'] == next_part]

        # Si next_part_df est vide, essayez avec part + 2
        if next_part_df.empty:
            next_part_df = df[df['vertex_par'] == part + 2]

        # Verifiez a nouveau si next_part_df n'est pas vide
        if not next_part_df.empty:
            last_of_next = next_part_df.iloc[-1]
            distance = calculer_distance(last_of_current, last_of_next)
            distances[last_of_current.name] = distance
        else:
            distances[last_of_current.name] = None
            print('ERREUR')
            break

    return distances

df['distance_last_to_last'] = distance_last_to_last(df)

# Sauvegarder le fichier modifie
df.to_csv(f'/Users/baptiste/Desktop/osm2qgis/csv/after/{nom_fichier}_final.csv', index=False)
