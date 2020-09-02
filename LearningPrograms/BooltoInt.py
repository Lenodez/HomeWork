def exactly_one_topping(ketchup, mustard, onion):
    return (ketchup + mustard + onion) == 1


print(exactly_one_topping(ketchup=True, mustard=False, onion=True))
