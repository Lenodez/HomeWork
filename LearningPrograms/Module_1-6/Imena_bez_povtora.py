name = 1
list_of_names =[]
while name != '':
    name = input()
    if name != '':
        list_of_names.append(name)
else:
    print(set(list_of_names))