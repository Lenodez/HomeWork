import random
pidor = int(input("Напиши целое число от 1 до 10 и узнаешь пидор ли ты "))
while pidor > 10 or pidor < 1:
    print('ТЫ чё даун? сказано больше 1 и меньше 10 ')
    pidor = int(input('от 1 сука, до 10 '))

proverka = random.randint(1, 10)

if proverka == pidor:
    print('Ты не пидор')
else:
    print('Ты пидор')

input('Нажми Enter ')

