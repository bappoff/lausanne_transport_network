import pandas as pd
import subprocess
import sys
import time

start_time = time.time()

def executer_scripts(nom_fichier):
    # Chemins des scripts
    script1 = '/Chemin/vers/calcul_distance.py'
    script2 = '/Chemin/vers/calcul_distance2.py'
    script3 = '/Chemin/vers/reorder.py'
    script4 = '/Chemin/vers/delete_col.py'
    script5 = '/Chemin/vers/filter_doublon.py'

    # Chemin du fichier CSV specifique
    csv_path = f'/Chemin/vers/le/fichier/contenant/les/noms/des/fichiers/csv/{nom_fichier}.csv'

    # Lire le fichier CSV specifique
    df = pd.read_csv(csv_path)


    # Calculer le nombre de valeurs uniques dans la colonne 'vertex_part'
    nombre_iterations = df['vertex_par'].nunique()


    # Executer le script 1, 4 et 5
    print('Debut d''execution sur le trace:',nom_fichier)
    subprocess.run(['python', script4, nom], check=True)
    subprocess.run(['python', script5, nom], check=True)
    subprocess.run(['python', script1, nom], check=True)

    # Boucle pour executer 25 fois le script 3 suivi du script 2
    for i in range(nombre_iterations + 10):
        subprocess.run(['python', script3, nom], check=True)
        subprocess.run(['python', script2, nom], check=True)
        print('Done ',i+1,"/",nombre_iterations+10)

# Lire le fichier avec les noms des fichiers a traiter
fichiers_df = pd.read_csv('/Chemin/vers/le/fichier/contenant/les/noms/des/fichiers/csv/')

# Iterer sur chaque nom de fichier et executer les scripts
for nom in fichiers_df['nom_fichier']:
    executer_scripts(nom)

end_time = time.time()

# Calcul de la duree totale
total_time_seconds = end_time - start_time

# Conversion en heures, minutes et secondes
hours = total_time_seconds // 3600
minutes = (total_time_seconds % 3600) // 60
seconds = total_time_seconds % 60

# Affichage du temps d'execution
print(f"Temps d'execution: {int(hours)} heures, {int(minutes)} minutes et {seconds:.2f} secondes")
