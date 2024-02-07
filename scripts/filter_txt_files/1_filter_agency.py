path_to_agency_file = '/Users/baptiste/Desktop/GTFS_241123/full/agency.txt'
path_to_filtered_agency_file = '/Users/baptiste/Desktop/GTFS_241123/agency.txt'

# Lire le fichier agency et ecrire les lignes correspondantes dans le nouveau fichier
with open(path_to_agency_file, 'r', encoding='utf-8') as agency_file, \
     open(path_to_filtered_agency_file, 'w', encoding='utf-8') as outfile:
    # Ecrire l'en-tete dans le nouveau fichier
    header = next(agency_file)
    outfile.write(header)
    
    # Ecrire les lignes qui contiennent "151" dans la colonne agency_id
    for line in agency_file:
        if line.strip() and (line.split(',')[0].strip('"') == "151" or line.split(',')[0].strip('"') == "55"):
            outfile.write(line)

print(f"Le filtrage est termine. Les donnees filtrees sont enregistrees dans {path_to_filtered_agency_file}")
