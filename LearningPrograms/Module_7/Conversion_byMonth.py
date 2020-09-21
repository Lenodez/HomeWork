import csv

# name.csv ниже нужно заменить на название csv файла, который вы хотите открыть

with open('click_stream3.csv', mode='r') as csv_file:  # открываем файл
    csv_reader = csv.DictReader(csv_file, fieldnames=['ID', 'page', 'date'])  # читаем файл

    funnel_by_month = {}  # Словарь для хранения данных
    funnel_template = {'1_home_page': 0, '2_search_page': 0, '3_payment_page': 0, '4_payment_confirmation_page': 0}

    for row in csv_reader:  # перебираем по одной строчке нашего файла
        page = list(row.items())[1][1]
        month = list(row.items())[2][1][:-3]
        if month not in funnel_by_month:
            funnel_by_month[month] = funnel_template.copy()

        if page == '1_home_page':
            funnel_by_month[month]['1_home_page'] += 1
        elif page == '2_search_page':
            funnel_by_month[month]['2_search_page'] += 1
        elif page == '3_payment_page':
            funnel_by_month[month]['3_payment_page'] += 1
        else:
            funnel_by_month[month]['4_payment_confirmation_page'] += 1

print(funnel_by_month)
