def Odd(k):
    if k == 1:
        return 1
    else:
        return Odd(k-1) + 2

print Odd(3)
