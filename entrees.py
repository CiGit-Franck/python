def dire_bonjour(prenom):
  return "Bonjour " + prenom

prenom_utilisateur = input("Bonjour, comment t'appelles-tu ? ")

print(dire_bonjour(prenom_utilisateur))

# Lire une ligne
f = open('convention.md', 'r')
print(f.readline())
f.close()

# Lire toutes les lignes
f = open('./convention.md', 'r')

for line in f:
    print(line)

f.close()

# Plus propre : open() fera la fermeture automatique
with open('./convention.md', 'r') as f:
  for line in f:
    print(line)

print('end')

f = open('./output.data', 'w')
f.write('Mon premier fichier écrit en Python')
f.close()

## Etape 7 : EntrÃ©es / Sorties

# - CrÃ©er un programme qui demande Ã  l'utilisateur de se prÃ©senter : prÃ©nom, nom et age. Utilisez la console pour afficher un message d'accueil personnalisÃ© du type "Bonjour _Jules Grand_ tu as _30 ans_ c'est bien Ã§a ?"
def presentation(prenom, nom, age):
  return "Bonjour " + prenom + " " + nom + " tu as " + age + " ans"

prenom = input("Prenom ? ")
nom = input("Nom ? ")
age = input("Age ? ")

print(presentation(prenom, nom, age))



# - CrÃ©er un programme qui fera la mÃªme chose tout en Ã©crivant les informations reÃ§ues dans un fichier texte. Le fichier devra Ãªtre nommÃ© _prenom-nom.txt_
# - CrÃ©er un programme qui va lire le fichier [films-2018.txt](../ressource/films-2018.txt) et indiquer combien il y a de films sortis en 2018.

# **Bonus**

# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et indiquer combien de fois apparaÃ®t _TOULOUSE_ dans le fichier.
# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et crÃ©er un nouveau fichier sans doublons (aprÃ¨s modification, le nouveau fichier ne doit contenir qu'une seule fois le mÃªme nom de ville).
# - CrÃ©er un programme qui va lire le fichier [villes-france.txt](../ressource/villes-france.txt) et crÃ©er un nouveau fichier dans lequel chaque ligne donnera le nom d'une ville en affichant le nombre dâ€™occurrence dans le fichier de dÃ©part. Ce fichier devra Ãªtre triÃ© par ordre alphabÃ©tique.

