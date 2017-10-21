# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.


def padding(S, mypad):
	result = “”
	for x in S:
		result += x + mypad
     result = result[:-1]
	#start @ end $
	return "@"+result+"$"

'''
Whenever S palindrome centered at i expands past the right bound of the palindrome centered at C (in other words, if it expands past R), C is assigned the value of i and R is updated according to the content of P[i] and i itself.
'''

def manacher(S,mypad):	
	#Preprocessing
	T=padding(S,mypad)
	P = [0]*len(T)
	#center index of longest palindrome calculated so far
	C = 0
	#right index of palindrome calculated so far	
	R = 0

	#Find the length of the longest palindrome that each index
	for i in range(1,len(T)-1):
		#Step 1: Take advantage of the work do so far
		# i < R, we can already seen T[i]
		if i < R:
			#length of mirror 
			mirror = 2*C - i
			#min length of palindrome at index i
			P[i] = min(P[mirror], R-i)

		#Step 2: Expand with i as the center of both sides
		#T has start @ end $  - while loop will break, no need to check both ends	 
		while T[i + P[i]] == T[i - P[i]]:
			P[i] +=1

		#Step 3: Find new C and R
		if (P[i] + i > R):
			C = i
			R = P[i] +i

	#Find the longest length (from the center)
	#Construct the left and right of the palindrome 
	center = 0
	length = 0
	for i in range(len(P)):
		if P[i] > length:
			length = P[i]
			center = i
	start = T[center-length+1:center]
	end = T[center:center+length]
	t = start+end
	#replace mypad		
	return t.replace(mypad,"")

S ="abaccddccefeg"
mypad="#"
print "Longest palindromic substring: ", manacher(S,mypad)
