# Etape 6 : Boucles

# Parcourir la liste prÃ©cÃ©dente. Pour chaque prÃ©nom, afficher la longueur du prÃ©nom avec la fonction **len**.
# Ajouter une variable **maximum** au dÃ©but du programme qui vaut 0 au dÃ©but. Pour chaque prÃ©nom, **si** la longueur du prÃ©nom est supÃ©rieur au maximum, remplacer maximum par cette valeur.
# Afficher le prÃ©nom le plus long Ã  la fin avec un message : "le prÃ©nom le plus long est <prÃ©nom>, il possÃ¨de <nbLettres> lettres"

prenoms_promo = ["Andrea", "Carole", "Nicolas", "Franck L",
                 "Franck T", "Vincent", "Jean-Marc", "Nicolas", "Guillaume",
                 "Philippe", "Yves", "Benoît", "Pierre", "Sylvain", "Frédéric"]
maximum = 0
prenoms = []

for prenom in prenoms_promo:
    longueur = len(prenom)
    print(prenom + " contient "+str(longueur) + " caractères ")
    if longueur > maximum:
        maximum = longueur
        prenoms.append(prenom)

print
print("le prenom le plus long est " +
      prenoms[0, len(prenoms)+1]+", il possede "+str(maximum)+" lettres")
