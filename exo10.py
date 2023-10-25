def tri_select(maliste):
    x=len(maliste)
    for i in range(x):
        a=maliste[i]
        j=i
        while j>0 and maliste[j-1]>a:
            maliste[j]=maliste[j-1]
            j=j-1
        maliste[j]=a
    print(maliste)

tri_select([3,2,1,8,5])