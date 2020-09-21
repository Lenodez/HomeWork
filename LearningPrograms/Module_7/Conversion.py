import csv

# name.csv ниже нужно заменить на название csv файла, который вы хотите открыть

with open('click_stream.csv', mode='r') as csv_file:  # открываем файл
    csv_reader = csv.DictReader(csv_file, fieldnames=['ID', 'page', 'date'])  # читаем файл
    funnel = {} # Словарь для хранения данных
    for row in csv_reader:  # перебираем по одной строчке нашего файла
        page = list(row.items())[1][1]
# так можно получить первый (не нулевой) элемент строки - для нашего датасета это строка, указывающая, на какой страничке было совершено действие
        if page not in funnel:
            funnel[page] = 1
        else:
            funnel[page] += 1
print(funnel)


