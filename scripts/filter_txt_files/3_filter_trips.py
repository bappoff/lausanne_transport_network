path_to_routes_file = '/Users/baptiste/Desktop/GTFS_241123/routes.txt'
path_to_trips_file = '/Users/baptiste/Desktop/GTFS_241123/full/trips.txt'
path_to_filtered_trips_file = '/Users/baptiste/Desktop/GTFS_241123/trips.txt'

# Lire le fichier routes et stocker les route_id dans un ensemble
route_ids = set()
with open(path_to_routes_file, 'r', encoding='utf-8') as routes_file:
    next(routes_file)  # Ignorer l'en-tete
    for line in routes_file:
        route_id = line.split(',')[0].strip('"')
        route_ids.add(route_id)

# Lire le fichier trips et conserver les lignes avec les route_id correspondants
with open(path_to_trips_file, 'r', encoding='utf-8') as trips_file, \
     open(path_to_filtered_trips_file, 'w', encoding='utf-8') as outfile:
    header = next(trips_file)
    outfile.write(header)  # ecrire l'en-tete dans le fichier de sortie
    for line in trips_file:
        if line.split(',')[0].strip('"') in route_ids:  # Verifier si route_id correspond
            outfile.write(line)

print(f"Le filtrage est termine. Les donnees filtrees sont enregistrees dans {path_to_filtered_trips_file}")
