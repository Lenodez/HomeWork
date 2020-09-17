def sum_posl(chislo):
    if chislo == (1 or 2):
        return 1
    chislo_pred = sum_posl(chislo-1)
    return chislo + chislo_pred
print(sum_posl(8))

