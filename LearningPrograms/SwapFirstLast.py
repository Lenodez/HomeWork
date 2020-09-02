racers = ['Mario', 'Luigi', 'Waluigi', 'DonkeyKong']


def swap(rac):
    hold = rac[0]
    rac[0] = rac[-1]
    rac[-1] = hold
    return rac


def swap_alt(rac):
    rac[0], rac[-1] = rac[-1], rac[0]
    return rac


print(swap_alt(racers))
input()
