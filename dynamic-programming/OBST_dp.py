# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def OBST(A, F, get_bst=False):
    n = len(A)
    table = [[None] * n for _ in xrange(n)]
    for i in xrange(n):
        table[i][i] = (F[i], i)
    # let optimal BST for subproblem A[i..j] be T
    # if table[i][j] = (cost, keyidx)
    # then cost is the cost of T, keyidx is index of the root key of T
    for s in xrange(1, n):
        for i in xrange(n-s):
            # compute cost for A[i..i+s]
            minimal, root = float('inf'), -1
            # search root with minimal cost
            freq_sum = sum(F[x] for x in xrange(i, i+s+1))
            for r in xrange(i, i+s+1):
                left = 0 if r == i else table[i][r-1][0]
                right = 0 if r == i+s else table[r+1][i+s][0]
                cost = left + right + freq_sum
                if cost < minimal:
                    minimal = cost
                    root = r
            table[i][i+s] = (minimal, root)
    if get_bst:
        tree = {}
        stack = [(0, n-1)]
        while stack:
            i, j = stack.pop()
            root = table[i][j][1]
            left, right = None, None
            if root != i:
                stack.append((i, root-1))
                left = table[i][root-1][1]
            if root != j:
                stack.append((root+1, j))
                right = table[root+1][j][1]
            if left is None and right is None:
                tree[root] = None
            else:
                tree[root] = (left, right)
        return (table[0][n-1][0], tree)

    return table[0][n-1][0]

if __name__ == '__main__':
    assert OBST([0, 1], [30, 40]) == 100
    assert OBST(['a', 'b', 'c'], [30, 10, 40]) == 130
    assert OBST([0, 1], [0.6, 0.4]) == 1.4
    assert OBST(range(1, 8), [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]) == 2.18
