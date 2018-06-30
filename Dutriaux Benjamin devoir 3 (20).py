# Félicitations pour ce très beau travail
# Il y a seulement une petite erreur lorsque l'on tape 3 pour quitter
# 20/20 

from random import random # Import de la fonction "random" générant un réel aléatoire allant de 0 à 1
from math import sqrt # Import de la fonction "racine carrée"
import sys # Import de la bibliothèque sys contenant une fonction permettant d'arreter le programme

while 1: # Boucle infinie permettant de revenir au début du programme à la fin de chaque exercice


    EstNumerique = True # Initialisation de la variable vérifiant que la valeur entrée est bien un entier

    print ("################################################################################")
    print ("")
    print ("Pour voir l'exercice 1, Tapez 1")
    print ("Pour voir l'exercice 2, Tapez 2")
    print ("Pour quitter le programme, Tapez 3")
    print ("")

    ChoixMenu1 = input () # Saisie du choix dans le menu d'acceuil

    try: # Tentative de conversion du choix en entier
        ChoixMenu1 = int (ChoixMenu1)

    except ValueError: # Code effectué en cas d'erreur
        EstNumerique = False
        print ("")
        print ("Erreur ! Veuillez entrer une valeur numérique.")
        print ("")



    if ChoixMenu1 == 1:

###############################
##        Exercice 1         ##
###############################

        print ("")
        print ("Pour voir la partie 1), tapez 1.")
        print ("Pour voir la partie 2), tapez 2.")
        print ("")
    
        ChoixMenu2 = input () # Saisie du choix dans le menu de l'exercice 1

        try: # Tentative de conversion du choix en entier
            ChoixMenu2 = int (ChoixMenu2)

        except ValueError: # Code effectué en cas d'erreur
            EstNumerique = False
            print ("")
            print ("Erreur ! Veuillez entrer une valeur numérique.")
            print ("")

        if ChoixMenu2 == 1:

    ###############################
    ##         Partie 1          ##
    ###############################
    
            Chaine = "" 


            print ("")
            for i in range (1, 11): # Boucle de changement de ligne
                Chaine = Chaine + " " +str(i) # Concaténation de chaines
                print (Chaine)
            print ("")
            
        elif ChoixMenu2 == 2:

    ###############################
    ##         Partie 2          ##
    ###############################
            
            print ("")
            for i in range (10, 0, -1): # Boucle de changement de ligne et de "reset" de la chaine
                Chaine = ""
                for j in range (1, i+1): # Boucle de concatenation
                    Chaine = Chaine + " " + str(j) # Concatenation de chaines
                print (Chaine)
            print ("")

        elif EstNumerique and (ChoixMenu1 != 1 or ChoixMenu1 != 2): # Erreur en cas de valeur numérique ne correspondant pas à un choix valide

            print ("")
            print ("Erreur ! Veuillez choisir une partie de l'exercice.")
            print ("")



    elif ChoixMenu1 == 2:

###############################
##        Exercice 2         ##
###############################

        print ("")
        print ("Pour voir la partie 1), tapez 1.")
        print ("Pour voir la partie 2), tapez 2.")
        print ("Pour voir la partie 3), tapez 3.")
        print ("")
    
        ChoixMenu2 = input () # Saisie du choix dans le menu de l'exercice 2

        try: # Tentative de conversion du choix en entier
            ChoixMenu2 = int (ChoixMenu2)

        except ValueError: # Code effectué en cas d'erreur
            EstNumerique = False
            print ("")
            print ("Erreur ! Veuillez entrer une valeur numérique.")
            print ("")


        if ChoixMenu2 == 1:

    ###############################
    ##         Partie 1          ##
    ###############################


            xA = random() # Génération de nombres aléatoires 
            xB = random()
            yA = random()
            yB = random()

            d = sqrt ((xB-xA)**2+(yB-yA)**2) # Calcul de la distance entre les points

            print ("")
            print ("La distance en le point A et le point B est : ",d)
            print ("")

        elif ChoixMenu2 == 2:

    ###############################
    ##         Partie 2          ##
    ###############################


            Total = 0 # Initialisation de la variable Total (Erreur sinon)

            for i in range (1, 1001):


                xA = random() # Génération de nombres aléatoires
                xB = random()
                yA = random()
                yB = random()

                d = sqrt ((xB-xA)**2+(yB-yA)**2) # Calcul de la distance entre les points


                Total = Total + d # Calcul du total de distance entre les points
    

            Moyenne = Total / 1000 # Calcul de la moyenne de distance entre les points
            print ("")
            print ("La moyenne des distances sur 1000 itérations est : ", Moyenne)
            print ("")


            # 5 essais avec le programme :
            #
            # 1 - 0.5452332972161673
            # 2 - 0.5055177282285583
            # 3 - 0.5198558467700221
            # 4 - 0.5244481681145353
            # 5 - 0.5307394788600653
            #
            # On peut remarquer que la moyenne se situe (presque) toujours entre 0.5 et 0.55.


        elif ChoixMenu2 == 3:

    ###############################
    ##         Partie 3          ##
    ###############################
        

            Total = 0 # Initialisation de la variable Total (Erreur sinon)

            print ("")
            print ("Cette opération peut prendre un peu de temps.")
            print ("")

            for i in range (1, 1000001):


                xA = random() # Génération de nombres aléatoires
                xB = random()
                yA = random()
                yB = random()

                d = sqrt ((xB-xA)**2+(yB-yA)**2) # Calcul de la distance entre les points


                Total = Total + d # Calcul du total de distance entre les points
    

            Moyenne = Total / 1000000 # Calcul de la moyenne de distance entre les points
            print ("")
            print ("La moyenne des distances sur 1000000 itérations est : ", Moyenne)
            print ("")

            # 5 essais avec le programme :
            #
            # 1 - 0.5212353069277696
            # 2 - 0.5210884310737804
            # 3 - 0.5216724644607645
            # 4 - 0.5211636818896205
            # 5 - 0.521580200127877
            #
            # Avec 1 000 000 itérations, la moyenne est encore plus précise, elle se situe entre 0.521 et 0.5217.
            


        elif EstNumerique and (ChoixMenu2 != 1 or ChoixMenu2 != 2 or ChoixMenu != 3): # Erreur en cas de valeur numérique ne correspondant pas à un choix valide
            
            print ("")
            print ("Erreur ! Veuillez choisir une partie de l'exercice.")
            print ("")

    elif ChoixMenu1 == 3: # Choix de quitter le programme
        
        sys.exit(0) # Fonction permettant de quitter le programme


    elif EstNumerique and (ChoixMenu1 != 1 or ChoixMenu1 != 2 or ChoixMenu != 3): # Erreur en cas de valeur numérique ne correspondant pas à un choix valide
        
        print ("")
        print ("Erreur ! Ce choix n'est pas valide.")
        print ("")
        

