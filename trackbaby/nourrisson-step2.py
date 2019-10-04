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

# print(poids_gars[1]) # debug

# Affichage des graphiques à faire
x = format_list(poids_gars[0])
plt.xlabel('Age en mois')
plt.grid()
# matrice de poids 
fig = plt.subplot(1, 3, 1)
fig.plot(x, format_list(poids_gars[1]), c='blue', linestyle = 'solid') # p5
fig.plot(x, format_list(poids_gars[2]), c='orange', linestyle = 'solid') # p25
fig.plot(x, format_list(poids_gars[3]), c='green', linestyle = 'solid') # p50
fig.plot(x, format_list(poids_gars[4]), c='red', linestyle = 'solid') # p75
fig.plot(x, format_list(poids_gars[5]), c='purple', linestyle = 'solid') # p95
fig.scatter(format_list(mesures[0]), format_list(mesures[1]), c='black') # mesures
plt.ylabel('Poids en kg')
# matrice de taille
fig = plt.subplot(1, 3, 2)
fig.scatter(format_list(mesures[0]), format_list(mesures[2]), c='black') # mesures
plt.ylabel('Taille en cm')
# matrice du perimetre cranien
fig = plt.subplot(1, 3, 3)
fig.scatter(format_list(mesures[0]), format_list(mesures[3]), c='black') # mesures
plt.ylabel('Perimetre cranien en cm')

plt.show()

