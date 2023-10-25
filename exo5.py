def fact(a):
    res=1
    for i in range(1,a+1):
        res=res*i
    return res

b=input("donnez un chiffre")
print(fact(int(b)))