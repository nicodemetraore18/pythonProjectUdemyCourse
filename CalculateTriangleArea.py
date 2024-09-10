a=float(input("Entrez le premier coté:"))
b=float(input("Entrez le deuxieme coté:"))
c=float(input("Entrez le troisieme coté:"))
s= (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is %0.2f"%area)
