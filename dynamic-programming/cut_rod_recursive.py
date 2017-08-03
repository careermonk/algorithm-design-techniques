def cut_rod(p, n):
    """
    Exponential-time, top-down recursive approach.
    """
    if n == 0:
        return 0
    else:
        r = float('-inf')
        # Consider a first cut of length i, for i from 1 to n inclusive
        for i in range(1, n+1):
            r = max(r, p[i] + cut_rod(p, n-i))
        return r

p = [0, 2, 8, 10, 12]
print  cut_rod(p, len(p)-1)
