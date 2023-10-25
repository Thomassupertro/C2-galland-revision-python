def dict_ecole(dictio):
    b=""
    a=-1
    for i in dictio:
        if(a!=-1):
            b=i
            a=dictio[i]
        else:
            if(dictio[i]>a):
                a=dictio[i]
                b=i
    print(b)


dicto = {
    "toto": 15,
    "fafa": 22,
}
dict_ecole(dicto)