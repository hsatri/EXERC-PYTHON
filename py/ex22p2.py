J=int(input("saisi le jour: "))
M=int(input("saisi le mois: "))
A=int(input("saisi le annee: "))
lnj=int
ln_m=int
ln_A =int
n=int


if (M==2 and J>28) or (J<1) or (J>31) or (M>12) or (M<1) or (A<1) :
    print("la date est incorrect")
elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12  :
            n=31
elif M==4 or M==6 or M==9 or M==11 :
                n=30
else :
                n=28

if J<n :
    lnj=J+1
    ln_m=M
    ln_A=A
elif M<12 and J>=n :
            ln_m=M+1
            ln_A=A
            lnj =1
else:
                    lnj = 1
                    ln_m = 1
                    ln_A = A+1



print("le lendmain est  :"+str(lnj))
print(":"+str(ln_m))
print(":"+str(ln_A))