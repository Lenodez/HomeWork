def delenie(a):
    while a > -2:
        try:
            b = 10 / a
            a -= 1
        except(ZeroDivisionError):
            print(a)
            a -= 1
    return a


# chsilo = int(input('Введите число ='))
# delenie(chsilo)


try:
    chsilo = int(input('Введите число ='))

    delenie(chsilo)
except(ZeroDivisionError):
    print('Ошибка возникает при a =', delenie(chsilo))
