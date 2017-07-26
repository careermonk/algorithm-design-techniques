from collections import deque
def get_boats(W, k):
	n = len(W)
	lanky = deque()
	bulky = deque()
	for i in xrange(n - 1):
		if W[i] + W[-1] <= k:
			lanky.append(W[i])
		else:
			bulky.append(W[i])
	bulky.append(W[-1])
	boats = 0
	while (lanky or bulky):
		if len(lanky) > 0:
			lanky.pop()
		bulky.pop()
		boats += 1
		if (not bulky and lanky):
			bulky.append(lanky.pop())
		while (len(bulky) > 1 and bulky[-1] + bulky[0] <= k):
			lanky.append(bulky.popleft())
	return boats

W = (5, 20, 21, 28, 39, 40, 65, 89, 98, 105)
print get_boats(W, 110)
