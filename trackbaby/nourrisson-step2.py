# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt

# csv pour lire les fichiers de données
import csv
import numpy as np

def format_list(list):
  return list[1:len(list)]

def convert_list_float(list):
  return list.astype(np.float)

def convert_list_int(list):
  return list.astype(np.int)

def x(list):
  return convert_list_int(format_list(list))

def y(list):
  return convert_list_float(format_list(list))

def matrice_csv(file):
  with open(file, 'r') as f:
    reader = csv.reader(f, delimiter=";")
    matrice = np.array(list(reader)) # charge la matrice 
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

# print(convert_list_int(poids_gars[0])) # debug

# Affichage des graphiques à faire
# matrice de poids 
poids = plt.subplot(1, 3, 1)
poids.plot(x(poids_gars[0]), y(poids_gars[1]), y(poids_gars[1]), c='#448abd', linestyle = 'solid', label='5%') # p5
poids.plot(x(poids_gars[0]), y(poids_gars[2]), c='#f29739', linestyle = 'solid', label='25%') # p25
poids.plot(x(poids_gars[0]), y(poids_gars[3]), c='#59a94a', linestyle = 'solid', label='50%') # p50
poids.plot(x(poids_gars[0]), y(poids_gars[4]), c='#cf4b3e', linestyle = 'solid', label='75%') # p75
poids.plot(x(poids_gars[0]), y(poids_gars[5]), c='#9f82c4', linestyle = 'solid', label='95%') # p95
poids.scatter(x(mesures[0]), y(mesures[1]), c='black') # mesures
plt.ylabel('Poids en kg')
plt.xlabel('Age en mois')
plt.legend()
plt.grid()
# matrice de taille
taille = plt.subplot(1, 3, 2)
taille.plot(x(tailles_gars[0]), y(tailles_gars[1]), c='#448abd', linestyle = 'solid', label='5%') # p5
taille.plot(x(tailles_gars[0]), y(tailles_gars[2]), c='#f29739', linestyle = 'solid', label='25%') # p25
taille.plot(x(tailles_gars[0]), y(tailles_gars[3]), c='#59a94a', linestyle = 'solid', label='50%') # p50
taille.plot(x(tailles_gars[0]), y(tailles_gars[4]), c='#cf4b3e', linestyle = 'solid', label='75%') # p75
taille.plot(x(tailles_gars[0]), y(tailles_gars[5]), c='#9f82c4', linestyle = 'solid', label='95%') # p95
taille.scatter(x(mesures[0]), y(mesures[2]), c='black') # mesures
plt.ylabel('Taille en cm')
plt.xlabel('Age en mois')
plt.legend()
plt.grid()
# matrice du perimetre cranien
crane = plt.subplot(1, 3, 3)
crane.plot(x(cranes_gars[0]), y(cranes_gars[1]), c='#448abd', linestyle = 'solid', label='5%') # p5
crane.plot(x(cranes_gars[0]), y(cranes_gars[2]), c='#f29739', linestyle = 'solid', label='25%') # p25
crane.plot(x(cranes_gars[0]), y(cranes_gars[3]), c='#59a94a', linestyle = 'solid', label='50%') # p50
crane.plot(x(cranes_gars[0]), y(cranes_gars[4]), c='#cf4b3e', linestyle = 'solid', label='75%') # p75
crane.plot(x(cranes_gars[0]), y(cranes_gars[5]), c='#9f82c4', linestyle = 'solid', label='95%') # p95
crane.scatter(x(mesures[0]), y(mesures[3]), c='black') # mesures
plt.ylabel('Perimetre cranien en cm')
plt.xlabel('Age en mois')
plt.legend()
plt.grid()

plt.show()

# :/devpt/python/analyse.py nourrisson-step2.py
# Traitement su fichier : nourrisson-step2.py
# Nombre de ligne vide : 13
# Nombre de ligne de commentaire : 13
# Nombre de fonctions : 6
# Nombre de ligne de code : 59
# Nombre de ligne total : 85
