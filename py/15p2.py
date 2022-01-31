c=input("entrer un caratere: " )
if c>='A' and c<='Z':
    c=c+'a'-'A'
if c>='a' and c<='z':
    c=c+'A'-'a'
print("le caratere apre transformation ",c)