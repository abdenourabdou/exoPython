# on defini nos fonctions, chaques fontions comprend
#def nomDeFonction () : 
# si on a besoin que notre fonction nous donne une reponse, 
# on ecrit return plus la valeur a returner 
def tapezLettre ():
    boite = input("tapez les characteres")
    # ici on renvoit la valeur contenu dans la boite qui contient
    # les characteres tapes 
    return boite

def tapezEntier ():
    boite = int(input("tapez un chiffre entier "))
    return boite

def tapezFloat ():
    boite = float(input("tapez un chiffre à virgule"))
    return boite



def tableMultiplication ( table ):
    multiplicateur = 1
    while multiplicateur <= 10:
        print (table * multiplicateur)
        multiplicateur = multiplicateur + 1

