# Etape 3
periode = "a definir"
heure = 15

if heure < 0 or heure > 24 :
    print("Erreur de saisie")
else:
    if heure < 10 :
        periode = "matinée"
    if heure < 18 :
        periode = "après midi"
    
    print("bonne "+periode)
