party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
who = 'Gilbert'


def fashionably_late(arrivals, name):
    order = arrivals.index(name)  # получаем ИНДЕКС формата число счет по arrivals идет с нуля
    if not order:
        print('None')
        return False
    else:
        return order >= len(arrivals) and order != len(arrivals) - 1


print(fashionably_late(party_attendees, 123))

