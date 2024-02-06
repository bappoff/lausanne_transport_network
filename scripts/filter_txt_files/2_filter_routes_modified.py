path_to_agency_file = '/Users/baptiste/Desktop/GTFS_241123/agency.txt'
path_to_routes_file = '/Users/baptiste/Desktop/GTFS_241123/full/routes.txt'
path_to_filtered_routes_file = '/Users/baptiste/Desktop/GTFS_241123/routes.txt'

# Lire le fichier agency et recuperer les agency_id
agency_ids = set()
with open(path_to_agency_file, 'r', encoding='utf-8') as file:
    next(file)  # Ignorer l'en-tete
    for line in file:
        agency_id = line.split(',')[0].strip('"')
        if agency_id:  # Verifier si l'agency_id existe
            agency_ids.add(agency_id)  # Ajouter tous les agency_id existants

# Lire le fichier routes et conserver les lignes avec les agency_id correspondants
with open(path_to_routes_file, 'r', encoding='utf-8') as routes_file, \
     open(path_to_filtered_routes_file, 'w', encoding='utf-8') as outfile:
    header = next(routes_file)
    outfile.write(header)  # ecrire l'en-tete dans le fichier de sortie
    for line in routes_file:
        if line.split(',')[1].strip('"') in agency_ids:  # Verifier si agency_id correspond
            outfile.write(line)

print(f"Le filtrage est termine. Les donnees filtrees sont enregistrees dans {path_to_filtered_routes_file}")