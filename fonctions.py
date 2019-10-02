## Etape 4 : CrÃ©ons des fonctions
import math

# aire d'un triangle 
def aire_triangle(base, hauteur):
    return (base * hauteur) / 2

# volume d'une sphere
def volume_sphere(rayon):
    return 4/3 * math.pi * rayon**3


# calcul d'IMC
def calcul_imc(prenom, poid, taille):
    imc = poid / ((taille/100) ** 2)
    return "IMC de "+prenom+" est de "+str(imc)

print("Aire du triangle vaut "+str(aire_triangle(12, 23)))
print("Volume de la sphere de rayon 12 vaut "+str(volume_sphere(12)))
print(calcul_imc("Joe", 40, 158))
