q=float(input("donner le nombre de piece :"))
p=float(input("donner le prix unitaire :"))
tc = p*q

if q>=100:
    mff = tc - tc * 0.2

elif q>=50 and q<100:
        mff = tc - 0.1 * tc
else :
    mff = tc

print("le montant final de la facture est : "+str(mff))