import math
P=float(input("donner le poids (kg): "))
T=float(input("donner la taille (cm): "))
IMC=P/math.sqrt(T)
PI=22*math.sqrt(T)
if IMC<18.5:
    E="MAIGRE"
if 18.5<IMC<25:
    E="NORMAL"
if IMC==22:
    E="IDEAL"
if IMC>30:
    E="Obese"
print("IMC="+str(IMC)+"\n")
print("Etat de sujet: ",E+"\n")
print("le paids ideal est: ",PI)