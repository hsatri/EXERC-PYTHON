I=int(input("saisir le nombre d'inscrit : "))
V=int(input("le nombre de votants : "))
Q=int(input("saisir le quorum : "))
P=(100*V)/I
M=(V/2)+1

if P>=Q:
    print("le votants est valide \n")
    print("le nombre de voix pour obtenir la majorite: "+str(M)+"\n")
    print("le pourcentage est: " +str(P))
else :
    print("le votants est non valide \n")