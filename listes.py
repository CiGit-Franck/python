## Etape 5 : Listes

# CrÃ©er une liste qui contient tous les prÃ©noms du groupe. Trier cette liste. Afficher tous les prÃ©noms qui ont un indice impair.
# CrÃ©er deux sous-listes `groupe_1` et `groupe_2` contenant chacun la moitiÃ© du groupe.

promo = ['benoit', 'franck L','philippe', 'guillaume', 'fred','carole','nicolas','pierre','saya','vincent','sylvain','jean marc', 'franck T', 'yben?']
print(promo)
print()
print(sorted(promo))
print()
print(promo)
print()
promo.sort()
print(promo)
print()

indice_impair = promo[1:len(promo)+1:2]

print(indice_impair)

groupe_1 = indice_impair
groupe_2 = promo[0:len(promo)+1:2]

# Correction de l'exercice maudit
def affiche_numero_couleur(carte_nb) :
    couleur = ["pique", "coeur", "carreau", "trefle"]
    valeur = ["7", "8", "9", "10", "valet", "dame", "roi", "as"]

    couleur_nb = carte_nb // 8
    valeur_nb = carte_nb % 8

    print("la carte est : "+valeur[valeur_nb] + " de " + couleur[couleur_nb])

print()
affiche_numero_couleur(28)

