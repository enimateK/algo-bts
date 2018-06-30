####################
##### Devoir 5 #####
####################

# Excellent travail.
# C2 vous donne la taille de la plus longue suite croissante moins un. Il faudrait rajouter 1.
#20 sur 20
from random import randint

Tx = []
C=0
C2=0

for i in range (0, 1000): #Remplissage du tableau de 1000 entiers entre 0 et 20

    Tx.append (randint(0,20))
    

for i in range (1, 1000):
    if Tx[i] >= Tx[i-1]: #Incrémentation si le nombre d'après est croissant
        C = C+1
        if C > C2: #Garde en mémoire la plus grande suite
            C2 = C
    else: #Remet à zéro si le nombre d'après est inférieur
        C=0

#print (Tx)
print ("")
print ("La plus grande suite croissante contient", C2, "termes")
print ("")

###############################################################
# Partie "Moyenne sur 10 itérations du programme"
###############################################################

Total = 0
Moyenne = 0

for i in range (0, 10):

    Tx = []

    for j in range (0, 1000): #Remplissage du tableau de 1000 entiers entre 0 et 20

        Tx.append (randint(0,20))
    
    C=0
    C2=0


    for j in range (1, 1000):
        if Tx[j] >= Tx[j-1]: #Incrémentation si le nombre d'après est croissant
            C = C+1
            if C > C2: #Garde en mémoire la plus grande suite
                C2 = C
        else: #Remet à zéro si le nombre d'après est inférieur
            C=0

    #print (Tx)
    #print ("La plus grande suite croissante contient", C2, "termes")
    Total = Total + C2

Moyenne = Total /10
print ("")
print ("La moyenne sur 10 executions du programme est : ",Moyenne)
print ("")

#############################################################################
# Partie "Moyenne sur 10 itérations du programme avec des entiers de 0 à 100"
#############################################################################

Total = 0
Moyenne = 0

for i in range (0, 10):

    Tx = []

    for j in range (0, 1000): #Remplissage du tableau de 1000 entiers entre 0 et 20

        Tx.append (randint(0,100))
    
    C=0
    C2=0


    for j in range (1, 1000):
        if Tx[j] >= Tx[j-1]: #Incrémentation si le nombre d'après est croissant
            C = C+1
            if C > C2: #Garde en mémoire la plus grande suite
                C2 = C
        else: #Remet à zéro si le nombre d'après est inférieur
            C=0

    #print (Tx)
    #print ("La plus grande suite croissante contient", C2, "termes")
    Total = Total + C2

Moyenne = Total /10
print ("")
print ("La moyenne sur 10 executions avec des entiers de 0 à 100 est :", Moyenne)
print ("")
print ("")
print ("On peut remarquer que les moyennes n'augmentent pas, que les entiers aillent de 0 à 20 ou de 0 à 100")
print ("")


