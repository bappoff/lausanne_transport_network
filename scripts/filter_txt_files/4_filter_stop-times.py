import csv

# Charger les trip_id valides du fichier trips.txt
def load_trip_ids(trips_file_path):
    with open(trips_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return {row['trip_id'] for row in reader}

# Charger les stop_id valides du fichier stops.txt
def load_stop_ids(stops_file_path):
    with open(stops_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return {row['stop_id'] for row in reader}

# Filtrer les lignes du fichier stop_times.txt base sur les trip_id et stop_id valides
def filter_stop_times(trips_file_path, stops_file_path, stop_times_file_path, output_file_path):
    # Charger les trip_id et stop_id valides
    valid_trip_ids = load_trip_ids(trips_file_path)
    valid_stop_ids = load_stop_ids(stops_file_path)
    
    # Ouvrir le fichier stop_times.txt et le fichier de sortie
    with open(stop_times_file_path, 'r', encoding='utf-8-sig') as stop_times, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as out_stop_times:
        
        # Preparer les objets CSV reader et writer avec le parametre pour conserver les guillemets
        stop_times_reader = csv.reader(stop_times, quotechar='"')
        out_stop_times_writer = csv.writer(out_stop_times, quoting=csv.QUOTE_NONE)  # Pour l'en-tete sans guillemets
        
        # ecrire l'entete sans guillemets
        headers = next(stop_times_reader)
        out_stop_times_writer.writerow(headers)
        
        out_stop_times_writer = csv.writer(out_stop_times, quoting=csv.QUOTE_ALL, quotechar='"')  # Pour les donnees avec guillemets

        # Filtrer chaque ligne du fichier stop_times.txt
        for row in stop_times_reader:
            trip_id, stop_id = row[0], row[3]
            # Verifier si les ids sont dans les listes valides
            stop_id_prefix = stop_id.split(":")[0]
            if trip_id in valid_trip_ids and stop_id_prefix in valid_stop_ids:
                row[3] = stop_id_prefix
                out_stop_times_writer.writerow(row)

# Chemins vers les fichiers
trips_file_path = '/Chemin/vers/le/fichier/filtered/trips.txt'  
stops_file_path = '/Chemin/vers/le/fichier/filtered/stops.txt'  
stop_times_file_path = '/Chemin/vers/le/fichier/original/stop_times.txt'  
output_file_path = '/Chemin/vers/le/nouveau/fichier/filtered/stop_times.txt'  

# Filtrer les stop_times et ecrire dans le fichier de sortie
filter_stop_times(trips_file_path, stops_file_path, stop_times_file_path, output_file_path)

print("Operation terminee !")
