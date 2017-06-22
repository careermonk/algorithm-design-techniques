def LCS(X, Y, i, j):
    if i == -1 or j == -1:
        return 0
    if X[i] == Y[j]:
        return 1 + LCS(X, Y, i-1, j-1)
    return max(LCS(X, Y, i-1, j), LCS(X, Y, i, j-1))

X = 'thisisatest'
Y = 'testingLCS123testing'
print (LCS(X, Y, len(X)-1, len(Y)-1))
