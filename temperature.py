choix = int(input("Tapez 1 pour C->F et 2 pour F->C"))
# 

if choix == 1:
    #---- on converti de celcius en far 
    c= int(input("Tapez une temperature en C°"))
    farenheit = (c*1.8)+32 # ici la formule trouver sur google 
    print(farenheit)

elif choix == 2:
    #---- on converti de far en celius  
    f= int(input("Tapez une temperature en F°"))
    celcius = (f-32)/1.8
    print(celcius)