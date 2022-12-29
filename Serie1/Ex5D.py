# demander à l'utilisateur de saisir une chaîne de caractères
s = input("Entrez une chaîne de caractères: ")

# créer un dictionnaire vide
d = {}

# parcourir les caractères de la chaîne
for c in s:
    # si le caractère est déjà présent dans le dictionnaire, incrémenter la valeur associée à la clé
    if c in d:
        d[c] += 1
    # sinon, ajouter le caractère au dictionnaire avec une valeur de 1
    else:
        d[c] = 1
# afficher le dictionnaire
print(d)


# Ce programme demande à l'utilisateur de saisir une chaîne de caractères, 
# puis crée un dictionnaire vide. Ensuite, il utilise une boucle for pour 
# parcourir les caractères de la chaîne. Si le caractère est déjà présent 
# dans le dictionnaire, la valeur associée à la clé est incrémentée de 1; 
# sinon, le caractère est ajouté au dictionnaire avec une valeur de 1. Enfin, 
# le programme affiche le dictionnaire.