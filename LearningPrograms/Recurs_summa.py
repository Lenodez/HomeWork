def sum_posl(end, shag):
    if end <= 0:
        return 0
    sum_m_shag = sum_posl(end=end - shag, shag=shag)
    return end + sum_m_shag


print(sum_posl(8, 2))
