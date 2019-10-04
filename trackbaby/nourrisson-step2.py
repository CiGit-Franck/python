# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt

# csv pour lire les fichiers de données
import csv
import numpy as np

def format_list(list):
  return list[1:len(list)]

def matrice_csv(file):
  with open(file, 'r') as f:
    reader = csv.reader(f, delimiter=";")
    matrice = np.array(list(reader))
    return np.transpose(matrice) # transpose / col 



# Récupération des mesures dans les fichiers à faire
# Relevé de mesures 
mesures = matrice_csv('./mesures.csv')
# constantes de poids
poids_fille = matrice_csv('./poids-age-fille-0-60-light.csv')
poids_gars  = matrice_csv('./poids-age-garcon-0-60-light.csv')
# constantes de tailles 
tailles_fille = matrice_csv('./taille-age-fille-0-60-light.csv')
tailles_gars  = matrice_csv('./taille-age-garcon-0-60-light.csv')
# constantes de périmètre cranien 
cranes_fille = matrice_csv('./perim-cra-age-fille-0-60-light.csv')
cranes_gars  = matrice_csv('./perim-cra-age-garcon-0-60-light.csv')

# print(format_list(poids_gars[0])) # debug

# Affichage des graphiques à faire
x = format_list(poids_gars[0])
# matrice de poids 
poids = plt.subplot(1, 3, 1)
poids.plot(x, format_list(poids_gars[1]), c='#448abd', linestyle = 'solid', label='5%') # p5
poids.plot(x, format_list(poids_gars[2]), c='#f29739', linestyle = 'solid', label='25%') # p25
poids.plot(x, format_list(poids_gars[3]), c='#59a94a', linestyle = 'solid', label='50%') # p50
poids.plot(x, format_list(poids_gars[4]), c='#cf4b3e', linestyle = 'solid', label='75%') # p75
poids.plot(x, format_list(poids_gars[5]), c='#9f82c4', linestyle = 'solid', label='95%') # p95
poids.scatter(format_list(mesures[0]), format_list(mesures[1]), c='black') # mesures
plt.ylabel('Poids en kg')
plt.xlabel('Age en mois')
plt.legend()
plt.grid()
# matrice de taille
taille = plt.subplot(1, 3, 2)
taille.scatter(format_list(mesures[0]), format_list(mesures[2]), c='black') # mesures
plt.ylabel('Taille en cm')
plt.xlabel('Age en mois')
plt.grid()
# matrice du perimetre cranien
crane = plt.subplot(1, 3, 3)
crane.scatter(format_list(mesures[0]), format_list(mesures[3]), c='black') # mesures
plt.ylabel('Perimetre cranien en cm')
plt.xlabel('Age en mois')
plt.grid()

plt.show()

