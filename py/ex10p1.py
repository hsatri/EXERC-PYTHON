q=int(input("donner la quantite: "))
Pu=float(input("donner le prix unitaire: "))
tc=q*Pu
if (tc>=500) :
    Sp=tc
else :
    Sp=tc+(0.1*tc)

print("Sp est: "+str(Sp))


