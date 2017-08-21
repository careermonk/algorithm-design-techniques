# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def sky_line(buildings):
    auxHeights = [0]*100
    rightMostBuildingRi=0
    for i, building in enumerate(buildings):
        left = int(building[0])
        height = int(building[1])
        right = int(building[2])
        for i in range(left,right):
            if(auxHeights[i]<height):
                auxHeights[i]=height    
        if(rightMostBuildingRi<right):
                    rightMostBuildingRi=right

    prev = 0
    for i in range(1,rightMostBuildingRi-1):
        if prev!=auxHeights[i]:
            print i, " ", auxHeights[i]
        prev=auxHeights[i]
    print rightMostBuildingRi, " ", auxHeights[rightMostBuildingRi]

buildings = [(1, 14, 7), (3, 9, 10), (5, 17, 12), (14, 11, 18), \
	(15, 6, 27), (20, 19, 22), (23, 15, 30), (26, 14, 29)]
sky_line(buildings)
