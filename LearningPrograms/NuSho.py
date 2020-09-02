import random

for i in range (10):
    python = random.randint(1, 100)
    ogorod = random.randint(1, 100)
    if python > ogorod:
        print('Учемся')
    else:
        print('Копаешь')
