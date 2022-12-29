employees = ['Abdelkrim', 'Fatima', 'Hicham', 'Karim', 'Loubna', 
'Mohammed', 'Noureddine', 'Oussama', 'Rachid', 'Salma', 'Youssef', 
'Zineb','Zineb','Zineb','Zineb', 'Gestion1', 'Gestion2', 'Gestion3', 'Gestion4', 'Gestion5']

# découper la liste en tranches de 5 éléments
for i in range(0, len(employees)-5, 5):
    # afficher les tranches de la liste, à l'exception des cinq derniers éléments (membres de la gestion)
    print(employees[i:i+5])