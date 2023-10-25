maliste=[]
for i in range(10):
    x=input("donnez une valeur \n")
    maliste.append(x)
def exo4(liste):
    a=maliste[0]
    b=maliste[0]
    moy=0
    for i in liste:
        if i>a:
            a=i
        if i<b:
            b=i
        moy+=int(i)
    moy=moy/10
    print("le maximum est : ", a, "le minimum est : ", b," et la moyenne est moy",moy)

exo4(maliste)