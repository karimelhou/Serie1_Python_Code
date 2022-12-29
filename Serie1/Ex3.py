ma_list = [1,2,2,1,5,6,8,10]

# loop over the elements of the list in reverse order
for i in range(len(ma_list)-1, -1, -1):
    # if the element is a duplicate, remove it from the list
    if ma_list.count(ma_list[i]) > 1:
        ma_list.pop(i)

# print the list without duplicates
print("List without duplicates:", ma_list)



# Pour chaque élément, le code utilise la méthode count() 
# de la liste pour compter le nombre de fois où l'élément 
# apparaît dans la liste. Si l'élément est en double, 
# il est supprimé de la liste à l'aide de la méthode pop().