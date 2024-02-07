import csv

# Charger les service_id valides du fichier trips.txt
def load_service_ids(trips_file_path):
    with open(trips_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return {row['service_id'] for row in reader}

# Filtrer les lignes du fichier calendar.txt base sur les service_id valides
def filter_calendar(trips_file_path, calendar_file_path, output_file_path):
    # Charger les service_id valides
    valid_service_ids = load_service_ids(trips_file_path)
    
    # Ouvrir le fichier calendar.txt et le fichier de sortie
    with open(calendar_file_path, 'r', encoding='utf-8-sig') as calendar, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as out_calendar:
        
        # Preparer les objets CSV reader et writer avec le parametre pour conserver les guillemets
        calendar_reader = csv.reader(calendar, quotechar='"')
        
        # Creer un writer pour l'en-tete sans guillemets
        out_calendar_writer = csv.writer(out_calendar, quoting=csv.QUOTE_NONE)
        
        # ecrire l'entete sans guillemets
        headers = next(calendar_reader)
        out_calendar_writer.writerow(headers)
        
        # Creer un nouveau writer pour les donnees avec guillemets
        out_calendar_writer = csv.writer(out_calendar, quoting=csv.QUOTE_ALL, quotechar='"')

        # Filtrer chaque ligne du fichier calendar.txt
        for row in calendar_reader:
            service_id = row[0]  # service_id est le premier champ
            # Si le service_id est dans la liste des service_id valides, ecrire la ligne dans le fichier de sortie
            if service_id in valid_service_ids:
                out_calendar_writer.writerow(row)

# Chemins vers les fichiers
trips_file_path = '/Chemin/vers/le/fichier/filtered/trips.txt'  
calendar_file_path = '/Chemin/vers/le/fichier/original/calendar.txt' 
output_file_path = '/Chemin/vers/le/fichier/filtered/calendar.txt'

# Filtrer le calendar et ecrire dans le fichier de sortie
filter_calendar(trips_file_path, calendar_file_path, output_file_path)

print("Done !")