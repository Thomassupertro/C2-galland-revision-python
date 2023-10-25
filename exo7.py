
def lectureFichier(monfichier):
    fichierlire = open(monfichier,"r")
    compt=0
    l1=fichierlire.readline()
    for i in l1:
        compt+=1
    f=open("fichierreponse.txt","w+")
    print(compt)
    f.write(str(compt))
a=input("donnez un nom de fichier oui\n")
lectureFichier(a)