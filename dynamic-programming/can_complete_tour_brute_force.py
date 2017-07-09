def can_complete_tour(gas, cost):
	if(len(gas) < 2): 
		return 0
	for i in range(len(gas)): # go from current node to the whole station
		balance = gas[i]
		canStart = True
		for j in range(1, len(gas)+1):
			balance -= cost[(i+j) % len(gas)] # travel to next station
			if(balance<0):
				canStart=False
				break
			balance += gas[(i+j) % len(gas)] # refuel
		if(canStart == True):
			return i
	return -1

gas = [15, 8, 2, 6, 18, 9, 21, 30]
cost = [8, 6, 30, 9, 15, 21, 2, 18]

print "We can start the tour from",can_complete_tour(gas, cost)
