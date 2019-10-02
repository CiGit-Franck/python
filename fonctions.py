## Etape 4 : CrÃ©ons des fonctions

# aire d'un triangle 
def aire_triangle(base, hauteur):
    return (base * hauteur) / 2

print("Aire du triangle vaut "+str(aire_triangle(12, 23)))

# calcul d'IMC
def calcul_imc(prenom, poid, taille):
    imc = poid / ((taille/100) ** 2)
    return "IMC de "+prenom+" est de "+str(imc)

print(calcul_imc("Joe", 40, 158))
