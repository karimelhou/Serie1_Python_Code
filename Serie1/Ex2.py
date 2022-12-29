ma_list = []

for i in range(700, 1100):
    if i % 7 == 0 and i % 5 != 0 and i % 2 !=0:
        ma_list.append(i)   


print (ma_list)
print (len(ma_list))
