def power_of_2(k):
    if k == 0:
        return 1
    else:
        return 2*power_of_2(k-1)

print power_of_2(3)
