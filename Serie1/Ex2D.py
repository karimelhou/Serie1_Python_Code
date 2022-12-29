dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9}
dicTablette = {"Sumsung3": 15 , "Other": 13}

newDic = {**dicPC, **dicPhone, **dicTablette}
print(newDic)


# Le code suivant crée trois dictionnaires dicPC, dicPhone et dicTablette, 
# puis utilise l'opérateur ** pour les fusionner en un seul dictionnaire newDic.