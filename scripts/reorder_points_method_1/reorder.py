import pandas as pd
import sys

# Recuperer le nom du fichier passe en argument
nom_fichier = sys.argv[1]  # Le premier argument est le nom du script, le second est votre argument

# Utiliser nom_fichier pour charger le fichier CSV correspondant
df = pd.read_csv(f'/Chemin/vers/le/fichier/enregistre/apres/execution/de/calcul_distance.py/{nom_fichier}_final.csv')

# Fonction pour determiner l'ordre
def determine_ordre(df):
    ordres = [None] * len(df)  # Initialiser une liste de la meme taille que le df
    traitement_special_effectue = False
    i = 0
    while i < len(df): #and df.iloc[i]['distance'] >= 50
        if not traitement_special_effectue and df.iloc[i]['distance_last_to_last'] < df.iloc[i]['distance']:
            # Traitement special pour la ligne actuelle et les lignes du vertex_part suivant
            ordres[i] = df.iloc[i]['vertex_ind']
            next_vertex_part = df.iloc[i]['vertex_par'] + 1
            next_part_rows = df[df['vertex_par'] == next_vertex_part]

            # Obtenir l'ordre inverse des vertex_index pour les lignes du vertex_part suivant
            reversed_indices = next_part_rows['vertex_ind'].iloc[::-1].tolist()
            for index in next_part_rows.index:
                ordres[index] = reversed_indices.pop(0)  # Assigner l'ordre inverse

            i += len(next_part_rows)  # Sauter les lignes deja traitees
            i += 1
            traitement_special_effectue = True
        else:
            # Pour toutes les autres lignes, utiliser simplement leur vertex_index
            ordres[i] = df.iloc[i]['vertex_ind']
            i += 1

    return ordres

# Ajouter la colonne ordre
df['ordre'] = determine_ordre(df)

# Trier le DataFrame en fonction de la colonne 'ordre'
df = df.sort_values(by='ordre')

# Remplacer les valeurs de 'vertex_index' par celles de 'ordre'
df['vertex_ind'] = df['ordre']


# Sauvegarder le fichier modifie
df.to_csv(f'/Chemin/vers/le/nouveau/fichier/csv/{nom_fichier}_step4.csv', index=False)
