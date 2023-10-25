phrase=input("Ecrivez moi une phrase")
print(phrase.lower())
print(phrase.upper())
compt=0
for i in phrase:
    if(i!=" "):
        compt=compt+1
print(compt)