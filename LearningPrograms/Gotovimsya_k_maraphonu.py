maraphon = int(input('Желаемая дистанция = '))
start = int(input('Но я могу = '))
procent = int(input('Буду увеличивать расстояния на столько процентов = '))
days = 1
while maraphon != int(start):
    start *= ((procent/100)+1)
    days += 1
else:
    print(days)