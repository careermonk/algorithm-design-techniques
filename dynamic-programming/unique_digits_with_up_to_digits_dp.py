def unique_digits(n):
        if n==0:
            return 1
        if n==1:
            return 10

        table = [0 for i in range(n+1)]
        table[0]=0
        table[1]=10
        table[2]=81
        total = table[0]+table[1]+table[2]
        for i in range(3,n+1):
		table[i] = table[i-1]*(10-i+1)
		total += table[i]
        return total

print unique_digits(2)
print unique_digits(3)
print unique_digits(4)
