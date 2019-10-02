# Etape 3
periode = "a definir"
heure = 19

if heure < 0 or heure > 24 :
    print("Erreur de saisie")
else:
    if heure < 10 :
        periode = "matinée"
    elif heure < 18 :
        periode = "après midi"
    else:
        periode = "soirée"
    
    print("bonne "+periode)
