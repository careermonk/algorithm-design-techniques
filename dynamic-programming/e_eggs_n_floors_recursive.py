import sys

def e_eggs_n_floors(floors, eggs):
    if eggs == 1 or floors < 2:
        return floors
    return min(1 + max(e_eggs_n_floors(i - 1, eggs - 1), e_eggs_n_floors(floors - i, eggs)) for i in xrange(1, floors))


print e_eggs_n_floors(100, 2)
