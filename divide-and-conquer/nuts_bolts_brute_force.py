def match_nuts_bolts(nuts, bolts):
	for i in range(len(nuts)):
		for j in range(len(bolts)):
			if nuts[i] ==  bolts [j]:
				print "Nut ", nuts[i], " matches with bolt ",  bolts [j]
		

nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
match_nuts_bolts(nuts, bolts)
