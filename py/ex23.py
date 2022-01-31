HD=int(input("donner l'heur de depart: "))
MD=int(input("donner minutes de depart: "))
HA=int(input("donner l'heur de arrivee: "))
MA=int(input("donner l'minutes de arrivee: "))


if (HD>HA and MD>MA):
            DH=(HA-HD)+24
            DM=60-MD+MA
if HD>HA and MD<MA :
        DH=HD-HA+24
        DM=MA-MD  #Incompréhensible
if (HD<HA and MD<MA):
                        DH=HA-HD #Incompréhensible
                        DM=60-MD+MA
if (HD<HA and MD>MA):
                        DH=HA-HD-1    #Incompréhensible
                        DM=60-MD+MA

print("la duree d'un trajet est : "+str(DH))
print(":"+str(DM))




