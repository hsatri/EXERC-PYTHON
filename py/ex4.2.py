H=int(input("entrer l'heur: "))
M=int(input("entrer minutes: "))
if M<59:
    ln_m=M+1
    ln_H=H
elif M==59 :
    ln_m=0
    ln_H=H+1
elif H==24 or (H==23 and M==59):
    ln_H=00
    ln_m=00
if H==24 :
    ln_H=00


print("le temps est: "+str(ln_H)+":"+str(ln_m))