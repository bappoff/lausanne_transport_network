import csv

# Charger les service_id valides du fichier trips.txt
def load_service_ids(trips_file_path):
    with open(trips_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return {row['service_id'] for row in reader}

# Filtrer les lignes du fichier calendar_dates.txt base sur les service_id valides
def filter_calendar_dates(trips_file_path, calendar_dates_file_path, output_file_path):
    # Charger les service_id valides
    valid_service_ids = load_service_ids(trips_file_path)
    
    # Ouvrir le fichier calendar_dates.txt et le fichier de sortie
    with open(calendar_dates_file_path, 'r', encoding='utf-8-sig') as calendar_dates, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as out_calendar_dates:
        
        # Preparer les objets CSV reader et writer avec le parametre pour conserver les guillemets
        calendar_dates_reader = csv.reader(calendar_dates, quotechar='"')
        
        # Creer un writer pour l'en-tete sans guillemets
        out_calendar_dates_writer = csv.writer(out_calendar_dates, quoting=csv.QUOTE_NONE)
        
        # ecrire l'entete sans guillemets
        headers = next(calendar_dates_reader)
        out_calendar_dates_writer.writerow(headers)
        
        # Creer un nouveau writer pour les donnees avec guillemets
        out_calendar_dates_writer = csv.writer(out_calendar_dates, quoting=csv.QUOTE_ALL, quotechar='"')

        # Filtrer chaque ligne du fichier calendar_dates.txt
        for row in calendar_dates_reader:
            service_id = row[0]  # service_id est le premier champ
            # Si le service_id est dans la liste des service_id valides, ecrire la ligne dans le fichier de sortie
            if service_id in valid_service_ids:
                out_calendar_dates_writer.writerow(row)

# Chemins vers les fichiers
trips_file_path = '/Users/baptiste/Desktop/GTFS_241123/trips.txt'
calendar_dates_file_path = '/Users/baptiste/Desktop/GTFS_241123/full/calendar_dates.txt'
output_file_path = '/Users/baptiste/Desktop/GTFS_241123/calendar_dates.txt'

# Filtrer le calendar_dates et ecrire dans le fichier de sortie
filter_calendar_dates(trips_file_path, calendar_dates_file_path, output_file_path)

print("Done !")