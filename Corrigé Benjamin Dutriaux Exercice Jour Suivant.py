# on peut parfois éviter les tests imbriqués
# le programme est très bien conçu, simple et clair.
# il est possible de gérer les erreurs de Python et d'afficher un message personnalisé
#*****************************************
# note : 19,5/20
#*****************************************

jour = int (input ("Saisir le jour : "))
mois = int (input ("Saisir le mois : "))
annee = int (input ("Saisir l'année : "))
test = 1
finmois = 0
finannee = 0
bissextile = 0

if annee%4 == 0:
    bissextile = 1
    if annee%100 == 0:
        bissextile = 0
        if annee% 400 == 0:
            bissextile = 1
#on peut faire aussi un seul test avec une condition complexe

if jour > 31 or jour < 1:
    message="Le jour doit être compris entre 1 et 31."
    test = 0
if mois > 12 or mois < 1:
    message="Le mois doit être compris entre 1 et 12."
    test = 0
if annee < 1582:
    message="La date ne doit pas être anterieure au 15/10/1582."
    test = 0
if annee == 1582:
    if mois <= 10:
        if jour <15:
            message="La date ne doit pas être anterieure au 15/10/1582."
            test = 0
if mois == 4 or mois == 6 or mois == 9 or mois == 11:
    if jour == 31:
        message="Ce mois ne contient que 30 jours."
        test = 0
if mois == 2:
    if jour > 28:
        message = "Il n'y a que 28 jours en Février cette année la."
        test = 0
        if bissextile == 1:
            if jour == 29:
                test = 1
            else:
                test = 0
                message="Il n'y a que 29 jours en Février lors d'une année bissextile."            






if test == 1:
    if jour == 31:
        finmois = 1
    if jour == 30 and (mois == 4 or mois == 6 or mois == 9 or mois == 11):
        finmois = 1
    if mois == 2:
        if jour >27:
            finmois = 1
        if bissextile == 1:
            if jour == 28:
                finmois = 0
    jour = jour + 1
    if finmois == 1: 
        jour = 1
        if mois == 12:
            finannee = 1
        mois = mois + 1
    if finannee == 1:
        mois = 1
        annee = annee + 1
    message = "Le jour suivant est", jour, mois, annee
    
        
        
print (message)
