J=int(input("saisi le jour: "))
M=int(input("saisi le mois: "))
A=int(input("saisi le annee: "))
lnj=int
ln_m=int
ln_A =int
N=int
A1 = M==4 or M==6 or M==9 or M==11

if (M==2 and J>28) or (J<1) or (J>31) or (M>12) or (M<1) or (A<1) or (A1 and J>30) :
    print("la date est incorrect")
elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12  :
            N=31
elif M==4 or M==6 or M==9 or M==11 :
                N=30


if J<N :
    lnj=J+1
    ln_m=M
    ln_A=A
elif M<12 and J>=N :
            ln_m=M+1
            ln_A=A
            lnj =1
else:       #pour le mois 12
                    lnj = 1
                    ln_m = 1
                    ln_A = A+1

if M == 2:
    if A % 4 == 0 and A % 100 != 0:
            if J < 29:
                            lnj = J + 1
                            ln_m = M
                            ln_A = A

            else:
                            ln_m = M + 1
                            ln_A = A
                            lnj = 1

    else:
            if J < 28:
                            lnj = J + 1
                            lnj = J + 1
                            ln_m = M
                            ln_A = A
            else:
                            ln_m = M + 1
                            ln_A = A
                            lnj = 1

print("jour-->"+str(lnj))
print("mois-->"+str(ln_m))
print("annee-->"+str(ln_A))