ma_List = ['karim','sara','someone','dog']

# méthode 1: utiliser une boucle for pour itérer sur les éléments de la liste
print("Méthode 1:")
for element in ma_List:
    print (element)
print ("--------------------------------")
# méthode 2: utiliser la fonction enumerate() avec une boucle for pour itérer sur 
# les éléments de la liste et obtenir les indices des éléments en même temps
print("\nMéthode 2:")
for i,element in enumerate(ma_List):
    print (element)