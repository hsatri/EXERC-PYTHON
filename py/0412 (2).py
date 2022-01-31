J = int(input("entrer le jour :"))
M = int(input("entrer le moi :"))
A = int(input("entrer le anne :"))
if M==4 and M==6 and M==9 and M==11 :
    if J<30:
            J=J+1
            M=M
            A=A
    else :
            J=1
            M=M+1
            A=A
if M == 1 and M == 3 and M == 5 and M == 7 and M==8 and M == 10:
    if J < 31:
        J = J + 1
        M = M
        A = A
    else:
        J = 1
        M = M + 1
        A = A
if M == 12:
    if J < 31:
        J = J + 1
        M = M
        A = A
    else:
        J = 1
        M = 1
        A = A+1

if M == 2:
    if A % 4 == 0 and A % 100 != 0:
        if J<29:
                J=J+1
                M = M
                A = A

        else:
                J = 1
                M = M + 1
                A = A

    else:
        if J < 28:
                J = J + 1
                M = M
                A = A
        else:
                J = 1
                M = M + 1
                A = A
print("le jour est :",J)
print("le mois est :",M)
print("l;anne est :",A)









