# définir le dictionnaire E
E = {"e1":13,"e2":17,"e3":9,"e4":15,"e5":8,"e6":7,"e7":16,"e8":12}

# créer les sous dictionnaires vides
Admis = {}
NonAdmis = {}

# parcourir les paires clé-valeur du dictionnaire E
for key, value in E.items():
    # si la moyenne est supérieure ou égale à 10, ajouter la paire clé-valeur au dictionnaire Admis
    if value >= 10:
        Admis[key] = value
    # sinon, ajouter la paire clé-valeur au dictionnaire NonAdmis
    else:
        NonAdmis[key] = value

# afficher les sous dictionnaires
print(Admis)
print(NonAdmis)


# Ce programme crée d'abord les sous dictionnaires Admis et NonAdmis vides, 
# puis utilise une boucle for pour parcourir les paires clé-valeur du dictionnaire E. 
# Si la moyenne est supérieure ou égale à 10, la paire clé-valeur est ajoutée au dictionnaire Admis; 
# sinon, elle est ajoutée au dictionnaire NonAdmis. Enfin, le programme affiche les sous dictionnaires.