catalan=[]

#1st term is 1
catalan.append(1)

for i in range (1,1001):
  x=catalan[i-1]*(4*i-2)/(i+1)
  catalan.append(x)

def catalan_number(n):
  return catalan[n]

print catalan_number(3)    
