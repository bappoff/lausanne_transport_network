import csv
import json

# Charge les donnees GeoJSON et renvoye un dictionnaire avec le nom de l'arret comme cle et les coordonnees comme valeur
def load_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        geojson_data = json.load(file)
    return {feature['properties']['ST_NOM']: feature['geometry']['coordinates'] for feature in geojson_data['features']}

# Fonction pour comparer les noms d'arrets, conserver les guillemets, remplacer les coordonnees, filtrer les stop_id, et supprimer le contenu de "parent_station"
def filter_stops(geojson_files, stops_file, new_stops_file, not_found_file):
    # Charger les noms d'arrets et les coordonnees des fichiers GeoJSON
    station_coords = {}
    for geojson_file in geojson_files:
        station_coords.update(load_geojson(geojson_file))
    
    # Ouvrir les fichiers necessaires
    with open(stops_file, 'r', encoding='utf-8') as stops, \
         open(new_stops_file, 'w', encoding='utf-8', newline='') as new_stops, \
         open(not_found_file, 'w', encoding='utf-8', newline='') as not_found:
        
        # Preparer les objets CSV reader et writer, en specifiant quotechar et quoting
        stops_reader = csv.reader(stops, quotechar='"')
        new_stops_writer = csv.writer(new_stops, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        not_found_writer = csv.writer(not_found, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # ecrire l'entete sans guillemets dans les deux nouveaux fichiers
        headers = next(stops_reader)
        new_stops_writer.writerow(headers)
        not_found_writer.writerow(headers)

        # Activer le quoting pour les lignes suivantes
        new_stops_writer = csv.writer(new_stops, quotechar='"', quoting=csv.QUOTE_ALL)
        not_found_writer = csv.writer(not_found, quotechar='"', quoting=csv.QUOTE_ALL)

        # Filtrer chaque ligne du fichier stops.txt
        for row in stops_reader:
            stop_id = row[0]
            stop_name = row[1]

            # Vider le contenu de la colonne "parent_station"
            row[-1] = ""

            # Verifier si stop_id contient uniquement des chiffres et pas de ":"
            if stop_id.isdigit() and ":" not in stop_id:
                # Si le nom de l'arret est trouve dans les donnees GeoJSON
                if stop_name in station_coords:
                    # Remplacer les coordonnees
                    row[2] = str(station_coords[stop_name][1])  # Latitude
                    row[3] = str(station_coords[stop_name][0])  # Longitude
                    new_stops_writer.writerow(row)
                else:
                    not_found_writer.writerow(row)
            else:
                not_found_writer.writerow(row)

# Chemin vers les fichiers GeoJSON et stops.txt
geojson_files = ['/Chemin/vers/le/fichier/bus_stations.geojson', '/Chemin/vers/le/fichier/metro_stations.geojson']
stops_file = '/Chemin/vers/le/fichier/original/stops.txt'

# Chemin vers les nouveaux fichiers
new_stops_file = '/Chemin/vers/le/nouveau/fichier/filtered/stops.txt'
not_found_file = '/Chemin/vers/le/fichier/notfound.txt'

# Appel de la fonction de filtrage
filter_stops(geojson_files, stops_file, new_stops_file, not_found_file)


print("Execution terminee !")
