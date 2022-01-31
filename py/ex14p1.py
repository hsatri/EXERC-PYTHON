import math
a=float(input("donner la valeur de a : "))
b=float(input("donner la valeur de b : "))
c=float(input("donner la valeur de c : "))
D=(b*b)-4*a*c
if D==0.0:
    X=-b/(2*a)
    print("la solution : ",X)
elif D>0:
    X1=((-b)-math.sqrt(D)/(2*a))
    X2 = ((-b) + math.sqrt(D) / (2 * a))
    print("le premiere solution est: ",X1)
    print("le premiere solution est: ", X2)
else :
    print("non solution")
