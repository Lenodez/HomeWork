kol_vo_sten = int(input('Количество стен: '))
perv_sten = int(input('Время за которое покрасиил первую стену: '))
i = 0
zatrachennoe_vremya = 0
while i != kol_vo_sten:
    zatrachennoe_vremya += perv_sten + 5 * i
    i += 1
if zatrachennoe_vremya % 60 == 0:
    print(zatrachennoe_vremya // 60)
else:
    print((zatrachennoe_vremya // 60) + 1)
