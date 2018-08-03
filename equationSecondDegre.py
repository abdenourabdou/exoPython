import math
from nosFonctions import *

#on utilise ici , notre focntion qui permet de recuperer un chiffre entier tape au clavier 
a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

# in sait que pour resoudre l'equation, on doit trouber le delta (google)
delta = (b*b) - 4*a*c # ici, la formule etouver sur google 
print("le delta = ", delta)

if delta > 0 : 
    print ("2 valeurs possible.")
    # si delta est plus grand que 0, on sait qu'on a 2 réponses 
    # et qu'il faut utilise les formules suivantes 
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("x1 = ",x1," x2= ",x2)

elif delta == 0 :
    print ("1 valeur possible")
     # si delta est plus egale a 0, on sait qu'on a 1 réponses 
    # et qu'il faut utilise les formules suivantes 
    x1 = -b  / (2*a)

    print("x = ",x1)

else:
    print("pas de réponse.")
    