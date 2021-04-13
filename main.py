mon_dictionnaire = {}

while True:
        try:
            taille=int(input("Entrer la taille du dictionnire:\t"))
            break
        except:
            print("Veuillez entrer un nombre !")

mon_dictionnaire = {n : n ** 2 for n in range(1,taille+1) }

print("Mon Dictionnaire est le ",mon_dictionnaire)
