def select_second(L):
    if len(L) >= 2:
        return L[1]
    return None


L = [2, 3, 5, 7]
k = [1]
print(select_second(k))
print(select_second(L))
