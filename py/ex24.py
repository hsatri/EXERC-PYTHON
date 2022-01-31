N1=int(input("donner la premiere nombre : "))
N2=int(input("donner la deusiem nombre : "))
N3=int(input("donner la troisiem nombre : "))
if (N1>N3>N2) :
    print(str(N1)+">"+str(N3)+">"+str(N2))
if (N2>N3 and N3>N1) :
    print(str(N2)+">"+str(N3)+">"+str(N1))
if (N1>N2 and N2>N3) :
    print(str(N1)+">"+str(N2)+">"+str(N3))
if (N2>N1 and N1>N3) :
    print(str(N2)+">"+str(N1)+">"+str(N3))
if (N3>N2 and N2>N1) :
    print(str(N3)+">"+str(N2)+">"+str(N1))
if (N3>N1 and N1>N2) :
    print(str(N3)+">"+str(N1)+">"+str(N2))
if (N1 >= N2 and N2 >= N3):
        print(str(N1) + ">" + str(N2) + ">" + str(N3))

