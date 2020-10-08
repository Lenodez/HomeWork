from random import randint, choice

class Lemming:
    # можно определять атрибуты на уровне класса, тогда они "привязаны" к классу
    total = 0

    def __init__(self):
        # обращаться - через именование класса
        Lemming.total += 1


family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = Lemming()
    family.append(new_lemming)
print(Lemming.total)