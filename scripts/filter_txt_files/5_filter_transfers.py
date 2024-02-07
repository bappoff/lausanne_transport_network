import csv

# Charger les stop_id valides du fichier stops.txt
def load_stop_ids(stops_file_path):
    with open(stops_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return {row['stop_id'] for row in reader}

# Filtrer les lignes du fichier transfers.txt base sur les stop_id valides
def filter_transfers(stops_file_path, transfers_file_path, output_file_path):
    # Charger les stop_id valides
    valid_stop_ids = load_stop_ids(stops_file_path)
    
    # Ouvrir le fichier transfers.txt et le fichier de sortie
    with open(transfers_file_path, 'r', encoding='utf-8-sig') as transfers, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as out_transfers:
        
        # Preparer les objets CSV reader et writer avec le parametre pour conserver les guillemets
        transfers_reader = csv.reader(transfers, quotechar='"')
        out_transfers_writer = csv.writer(out_transfers, quoting=csv.QUOTE_NONE)  # Pour l'en-tete sans guillemets
        
        # ecrire l'entete sans guillemets
        headers = next(transfers_reader)
        out_transfers_writer.writerow(headers)
        
        out_transfers_writer = csv.writer(out_transfers, quoting=csv.QUOTE_ALL, quotechar='"')  # Pour les donnees avec guillemets

        # Filtrer chaque ligne du fichier transfers.txt
        for row in transfers_reader:
            from_stop_id, to_stop_id = row[0], row[1]
            # Verifier si les stop_id sont dans la liste valide ET pour les deux stop_id
            if from_stop_id in valid_stop_ids and to_stop_id in valid_stop_ids:
                out_transfers_writer.writerow(row)

# Chemins vers les fichiers
stops_file_path = '/Users/baptiste/Desktop/GTFS_241123/stops.txt'  
transfers_file_path = '/Users/baptiste/Desktop/GTFS_241123/full/transfers.txt'  
output_file_path = '/Users/baptiste/Desktop/GTFS_241123/transfers.txt'

# Filtrer les transfers et ecrire dans le fichier de sortie
filter_transfers(stops_file_path, transfers_file_path, output_file_path)

print("Operation terminee")