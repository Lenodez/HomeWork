name = 1
list_of_names = []
kol_vo_par = 0;
while name != '':
    name = input()
    if not (name in list_of_names):
        list_of_names.append(name)
    else:
        list_of_names.remove(name)
        kol_vo_par += 1
else:
    print(kol_vo_par)
