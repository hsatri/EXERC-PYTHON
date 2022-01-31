choix=int(input("Taper 1 pour Dhs=>Euros \n Taper 2 pour Euros => Dhs \n Taper 3 pour quitter : \n"))
if choix==3:
    exit(0)
N=float(input("Entrer le montant a convertir : "))
if choix==1:
    N=N/10
if choix==2:
    N=N*10


print("le montant a convertir est :",N)