def cvet(BukvaCifra):
    bukvi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = int(bukvi.index(BukvaCifra[0]))
    y = int(BukvaCifra[1])
    return (x+y) % 2

pervaya = cvet(input('Введите кординаты первой клетки '))
vtoraya = cvet(input('Введите кординаты второй клетки '))
if pervaya == vtoraya:
    print('Клетки одного цвета')
