Pu=float(input("Entre le prix de la voiture: "))
Puissance=int(input("Entren la puissance de la voiture : "))

if Puissance<115 and Puissance>0 :
    TVA=0.25*Pu
else :
    TVA=0.33*Pu

print("la valeur de la tva est : "+str(TVA)+"\n")
print("la valeur de la tva est : ",(Pu+TVA))