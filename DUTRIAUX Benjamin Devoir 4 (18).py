#################
##  Devoir 4   ##
#################
#Très bien mais il falait utiliser le tableau Cx pour faire un bilan
#Voir code complémentaire ci-dessous
#18/20
from random import randint

Tx = []
Cx = []

for i in range (0, 1000):

    Tx.append (randint(0,1))


print ("")
print ("Suite de 1000 0 ou 1 générés aléatoirement :")
print ("")
print (Tx)
print ("")

C=0
C2 = 0

for i in range (0, 1000):
    if Tx[i] == 1:
        C = C+1
        if C > C2:
            C2 = C
    else:
        if C>0:
            Cx.append (C)
        C=0
if C>0:
    Cx.append (C)


print ("")
print ("Liste des suites de 1 :")
print ("")
print (Cx)
print ("")
#Il faudrait faire le compte des suites de 1 par longueur, à partir de Cx
#************************************************************************
bilan=[0]*max(Cx)
for i in range(0,len(Cx)):
    bilan[Cx[i]-1]=bilan[Cx[i]-1]+1
print(bilan)
for i in range(0,len(bilan)):
    print(bilan[i], " suites de 1 de longueur ", i+1)
#************************************************************************
print ("")
print ("Plus grande suite de 1 :")
print ("")
print (C2)
print ("")


    
# Pour la suite, créer deux compteur, un contenant la suite la plus grande et l'autre qui compte
# Une condition pour tester si le chiffre est un 1 ou un 0
# une boucle while (while T[i] = 1 Compteur + 1)
# Cas particulier : liste à la fin du tableau
