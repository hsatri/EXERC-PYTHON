import math
P=float(input("donner le poids: "))
T=float(input("donner le taille: "))

BMI=P/math.sqrt(T)
if BMI<= 27:
    c="normal"
if BMI> 27 and BMI<30:
    c="obese"
if BMI >= 30:
   c="malade"

print(c+":"+str(BMI)+" kg/m")