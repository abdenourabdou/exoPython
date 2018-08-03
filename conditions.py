
# on cree un variable qui est egale a 5
boite = 5

# si la variable boite est plus grande que 10 
if boite > 10 :
    # on affiche plus grand 
    print("plus grand")

# sinon , si 
elif boite < 10 :
    print("plus petit")

#sinon, en definitif, c'est que la vaariable egale 
else:
    print("egal")


#------------------
#exemple 2 

# on garde le reste de la division de 52 par 2 ( modulo)
# et on le stock le resultat dans la variable boite 
boite = 52 % 2

# si le contenu de la variable boite est egale a 0
#attention, double = qaund on compare 2 elements 
if boite == 0 :
    print(" 52 est un chiffre pair")