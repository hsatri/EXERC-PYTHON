A=int(input("donner la valeur de A: "))
B=int(input("donner la valeur de B: "))
print("choix 1. comparer deux entiers \n choix 2. somme de deux entiers \n choix 3. quitter \n")
choix=int(input("Taper le nombre de votre choix : "))
if choix==1:
    if A>=0 and B>=0:
        print("la somme est positive")
    if A<0 and B<0:
        print("la somme est negative")
    if A<0 and B>=0:
        if B>(-A):
            print("la somme est negative")
        else :
            print("la somme est negative")
    if A >= 0 and B < 0:
        if A > (-B):
            print("la somme est positive")
        else:
            print("la somme est negative")
if choix==2:
    S = A + B
    print("la somme est ",S)
if choix==3:
    exit(0)
