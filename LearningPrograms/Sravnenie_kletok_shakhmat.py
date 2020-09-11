def cvet(BukvaCifra):
    bukvi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = -1
    sum = -1
    while i < len(bukvi):
        i += 1
        if BukvaCifra[0] == bukvi[i]:
            sum = sum + int(BukvaCifra[1])
            sum += i
            break
    return sum % 2


pervaya = cvet(input('Введите кординаты первой клетки '))
vtoraya = cvet(input('Введите кординаты второй клетки '))
if pervaya == vtoraya:
    print('Клетки одного цвета')
