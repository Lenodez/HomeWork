import absx as b
print(b.f(-5))

spisok = input('Введите числа через запятую ')
spisok = spisok.split(',')
perebor = 0
maximum: int = int(spisok[0])
while len(spisok) > perebor:
    if int(spisok[perebor]) > maximum:
        maximum = int(spisok[perebor])
    perebor += 1
print(maximum)
