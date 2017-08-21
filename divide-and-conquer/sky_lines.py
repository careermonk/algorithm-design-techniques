# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if buildings==[]:
            return []
        if len(buildings)==1:
            return [[buildings[0][0],buildings[0][1]],[buildings[0][2],0]]
        mid=(len(buildings)-1)/2
        leftSkyline=self.getSkyline(buildings[0:mid+1])
        rightSkyline=self.getSkyline(buildings[mid+1:])
        return self.merge(leftSkyline,rightSkyline)

    def merge(self, leftSkyline, rightSkyline):
        i=0
        j=0
        resultSkyline=[]
        h1=None
        h2=None
        while i<len(leftSkyline) and j<len(rightSkyline):
            if leftSkyline[i][0]<rightSkyline[j][0]:
                h1=leftSkyline[i][1]
                new=[leftSkyline[i][0],max(h1,h2)]
                if resultSkyline==[] or resultSkyline[-1][1]!=new[1]:
                    resultSkyline.append(new)
                i+=1
            elif leftSkyline[i][0]>rightSkyline[j][0]:
                h2=rightSkyline[j][1]
                new=[rightSkyline[j][0],max(h1,h2)]
                if resultSkyline==[] or resultSkyline[-1][1]!=new[1]:
                    resultSkyline.append(new)
                j+=1
            else:
                h1=leftSkyline[i][1]
                h2=rightSkyline[j][1]
                new=[rightSkyline[j][0],max(h1,h2)]
                if resultSkyline==[] or resultSkyline[-1][1]!=new[1]:
                    resultSkyline.append([rightSkyline[j][0],max(h1,h2)])
                i+=1
                j+=1

        while i<len(leftSkyline):
            if resultSkyline==[] or resultSkyline[-1][1]!=leftSkyline[i][1]:
                resultSkyline.append(leftSkyline[i][:])
            i+=1

        while j<len(rightSkyline):
            if resultSkyline==[] or resultSkyline[-1][1]!=rightSkyline[j][1]:
                resultSkyline.append(rightSkyline[j][:])
            j+=1
            
        return resultSkyline

buildings = [[1, 14, 7], [3, 9, 10]]
sky_line = Solution()
print sky_line.getSkyline(buildings)
