
## Etape 7 : EntrÃ©es / Sorties

# - CrÃ©er un programme qui demande Ã  l'utilisateur de se prÃ©senter : prÃ©nom, nom et age. Utilisez la console pour afficher un message d'accueil personnalisÃ© du type "Bonjour _Jules Grand_ tu as _30 ans_ c'est bien Ã§a ?"
def presentation(prenom, nom, age):
  return "Bonjour " + prenom + " " + nom + " tu as " + age + " ans"

prenom = input("Prenom ? ")
nom = input("Nom ? ")
age = input("Age ? ")

print(presentation(prenom, nom, age))

# - CrÃ©er un programme qui fera la mÃªme chose tout en Ã©crivant les informations reÃ§ues dans un fichier texte. Le fichier devra Ãªtre nommÃ© _prenom-nom.txt_
with open('./convention.md', 'r') as f:
  for line in f:
    print(line)

# - CrÃ©er un programme qui va lire le fichier [films-2018.txt](../ressource/films-2018.txt) et indiquer combien il y a de films sortis en 2018.
nb_film = 0
with open('./films-2018.txt', 'r') as f:
  for line in f:
      nb_film = nb_film + 1

print("En 2018, il y a eu "+str(nb_film)+" films")

# **Bonus**

# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et indiquer combien de fois apparaÃ®t _TOULOUSE_ dans le fichier.
occurence = 0
recherche = input("Rechercher ?")

def occurence_existe(ligne):
    return recherche in ligne

with open('./villes-france.txt', 'r') as f:
  for line in f:
      if occurence_existe(line):
        occurence = occurence + 1

print(recherche + " est present "+str(occurence)+" fois ")

# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et crÃ©er un nouveau fichier sans doublons (aprÃ¨s modification, le nouveau fichier ne doit contenir qu'une seule fois le mÃªme nom de ville).
# doublons = []
# with open('./villes-france.txt', 'r') as f:
#   for line in f:
#       if occurence_existe(line):
#         occurence = occurence + 1

# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et crÃ©er un nouveau fichier dans lequel chaque ligne donnera le nom d'une ville en affichant le nombre dâ€™occurrence dans le fichier de dÃ©part. Ce fichier devra Ãªtre triÃ© par ordre alphabÃ©tique.

