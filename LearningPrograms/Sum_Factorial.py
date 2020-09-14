x = int(input('Введите число для подсчёта суммы факториалов: '))
i = 0
summa = 0
chast_summa = 1
while x != i:
    i += 1
    chast_summa *= i
    summa += chast_summa
else:
    print('Сумма факториалов = ', summa)

