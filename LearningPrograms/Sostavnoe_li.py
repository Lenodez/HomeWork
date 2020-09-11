def prostoe_li(chislo):
    delitel = 2
    while chislo % delitel != 0:
        delitel += 1
    return delitel == chislo

chiselko = int(input('Введите число '))
if prostoe_li(chiselko) == True:
    print('Простое')
else:
    print('Составное')