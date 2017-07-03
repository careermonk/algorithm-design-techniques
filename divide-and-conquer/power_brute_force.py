def power_brute_force(a, n):
    """linear power algorithm"""
    x = a
    for i in range(1, n):
        x *= a
    return x

print power_brute_force(2, 3)
