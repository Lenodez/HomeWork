storona = int(input('Введите длину стороны квадрата: '))
simvol = input('Введите символ для рисования: ')
for i in range(1, storona+1, 1):
    stroka = []
    j = 0
    while j != storona:
        stroka.append(' ')
        j += 1
    stroka[(i-1)] = simvol
    stroka[(storona-i)] = simvol
    vivod = ''
    for k in range(0, storona, 1):
        vivod += stroka[k]
    print(vivod)