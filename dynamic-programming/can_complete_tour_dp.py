def can_complete_tour(gas, cost):
	if(len(gas) < 2):
		return -1
	pre = len(gas)-1
	end = 0
	gas_balance = gas[end] - cost[end]
	while(pre != end): 		# extand the path [pre+1, end] to full path
		if(gas_balance < 0) : 	# if gas_balance is not enough to go to next station
			gas_balance += gas[pre] - cost[pre]
			pre = (pre + len(gas) - 1) % len(gas) # extend to previous station
		else :
			end = (end + 1) % len(gas) # extend to next station
			gas_balance += gas[end] - cost[end]

	if gas_balance < 0:
		return -1
	else:
		return (pre+1) % len(gas)

gas = [15, 8, 2, 6, 18, 9, 21, 30]
cost = [8, 6, 30, 9, 15, 21, 2, 18]

print "We can start the tour from",can_complete_tour(gas, cost)
