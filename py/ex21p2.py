S=int(input("donner les secondes :"))

M=S/60
S=S%60
H=M/60
M=M%60
J=H/24

print("le temps est: "+str(J)+":"+str(H)+":"+str(M)+":"+str(S))