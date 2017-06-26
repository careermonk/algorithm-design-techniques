# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2017-06-02 06:15:46 
# Last modification		: 2017-06-02 
# Modified by		        : Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				 warranty; without even the implied warranty of 
# 				 merchantability or fitness for a particular purpose. 

def match_nuts_bolts(nuts, bolts):
	for i in range(len(nuts)):
		for j in range(len(bolts)):
			if nuts[i] ==  bolts [j]:
				print "Nut ", nuts[i], " matches with bolt ",  bolts [j]
		

nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
match_nuts_bolts(nuts, bolts)
