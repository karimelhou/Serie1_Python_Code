# définir la liste d'entiers
l = [1, 2, 3, 4, 5, 6]

# créer un dictionnaire vide
d = {}

# parcourir les entiers de la liste
for n in l:
    # si l'entier est pair, ajouter la paire clé-valeur au dictionnaire avec la valeur 'pair'
    if n % 2 == 0:
        d[n] = 'pair'
    # sinon, ajouter la paire clé-valeur au dictionnaire avec la valeur 'impair'
    else:
        d[n] = 'impair'

# afficher le dictionnaire
print(d)

# Ce programme définit d'abord une liste d'entiers, puis crée un dictionnaire vide. Ensuite, 
# il utilise une boucle for pour parcourir les entiers de la liste. Si l'entier est pair,
# la paire clé-valeur est ajoutée au dictionnaire avec la valeur 'pair'; sinon, elle est ajoutée au 
# dictionnaire avec la valeur 'impair'. Enfin, le programme affiche le dictionnaire.