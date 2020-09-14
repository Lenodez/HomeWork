uchastniki_komandi = []
kol_vo_uchastnikov = 6
uchast_seychas = 0
while uchast_seychas != kol_vo_uchastnikov:
    pol = input('Введите ваш пол м или ж ')
    if pol == 'ж':
        vozrast = int(input('Введите ващ возраст '))
        if 36 > vozrast > 17:
            print('Вы в команде!')
            uchast_seychas += 1
            uchastniki_komandi.append(pol + str(vozrast))
        else:
            print('Извините, но вы не подходите :( ')
    else:
        print('Извините, но ы не подходите :(')
else:
    print(uchastniki_komandi)