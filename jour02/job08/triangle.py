a=0
b=0
c=0
resultat1=False
resultat2=False
resultat3=False
a=float(input("rentrez a : "))
b=float(input("rentrez b : "))
c=float(input("rentrez c : "))

if a + b > c:
    resultat1=True
elif a + c > b:
    resultat2=True
elif b + c > a:
    resultat3=True
else:
    print("nous n'avons pas un triangle")

if resultat1 == True and resultat2 == True and resultat3 == True:
    print("nous avons un trinagle")