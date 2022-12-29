# demander à l'utilisateur de saisir une chaîne de caractères
s = input("Entrez une chaîne de caractères: ")

# créer un dictionnaire vide
d = {}

# parcourir les caractères de la chaîne
for i, c in enumerate(s):
    # si le caractère n'est pas déjà présent dans le dictionnaire, l'ajouter au dictionnaire avec la position en valeur
    if c not in d:
        d[c] = i

# afficher le dictionnaire
print(d)


# Ce programme demande à l'utilisateur de saisir une chaîne de caractères, 
# puis crée un dictionnaire vide. Ensuite, il utilise une boucle for avec l'instruction enumerate() 
# pour parcourir les caractères de la chaîne et leur index. Si le caractère n'est pas déjà présent 
# dans le dictionnaire, il est ajouté au dictionnaire avec la position en valeur. Enfin, le programme 
# affiche le dictionnaire.