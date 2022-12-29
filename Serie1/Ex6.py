ma_list= [17, 38, 10, 25, 72]

ma_list.sort()
ma_list.reverse()
print(ma_list.index(17))
ma_list.pop(ma_list.index(38))
print(ma_list)

sous_list = ma_list[1:3]
print(sous_list)
sous_list = ma_list[:2  ]
print(sous_list)
sous_list = ma_list[2:]
print(sous_list)
sous_list = ma_list
print(sous_list)
print(sous_list[-1])
