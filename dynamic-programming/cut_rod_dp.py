def cut_rod(p, n):
	r = (n + 1) * [0]
	for j in range(1, n+1):
		q = float('-inf')
		for i in range(1, j+1):
			q = max(q, p[i] + r[j-i])
		r[j] = q
	return r[n]

p = [0, 2, 8, 10, 12]
print  cut_rod(p, len(p)-1)
