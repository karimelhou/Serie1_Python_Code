n = int(input("Entrez un entier n: "))

# créer un dictionnaire vide
d = {}

# ajouter les paires clé-valeur au dictionnaire
for i in range(1, n+1):
    d[i] = i**2

# afficher le dictionnaire
print(d)