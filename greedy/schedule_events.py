class Event(object):
	def __init__(self, deadline, profit):
		self.deadline = deadline
		self.profit = profit

	def __repr__(self):
		return str((self.deadline, self.profit))

def schedule_events(E):
	E.sort(lambda x, y: y.profit - x.profit) 
	
	X = []
	totalProfit = 0
	slot = 0
	for i in E:
		if slot <= i.deadline:
			totalProfit += i.profit
			X.append(i)
			slot += 1

	return X, totalProfit

if __name__ == '__main__':
    E = []
    E.append(Event(1, 3))
    E.append(Event(3, 8))
    E.append(Event(4, 8))
    E.append(Event(4, 10))
    X, profit = schedule_events(E)
print "Schedule", X, "got the profit", profit
