"""All Pairs Shortest Paths with matrix multiplication"""
def create_matrix(n, m, fill_with=0):
    """Create an n-times-m matrix that is filled with fill_with."""
    result = []
    for i in xrange(n):
        row = []
        for j in xrange(m):
            row.append(fill_with)
        result.append(row)
    return result

def get_dimensions(M):
    """Get the dimensions of matrix M."""
    n = len(M)
    if n == 0:
        return (0,0)
    m = len(M[0])
    return (n,m)

def get_num_rows(M):
    n,m = get_dimensions(M)
    return n

def get_num_cold(M):
    n,m = get_dimensions(M)
    return m

def clone(M):
    n,m = get_dimensions(M)
    C = create_matrix(n,m)
    for i in xrange(n):
        for j in xrange(m):
            C[i][j] = M[i][j]
    return C

def __get_pattern(x, infinity):
    return str(x)

def print_matrix(M, infinity=None):
    """Print matrix M

    For example:
    
    [ 0 1 2 ]
    [ 3 4 5 ]
    [ 6 7 8 ]
    """
    
    if len(M) > 0:
        maxlen = {}
        for row in M:
            for j in xrange(len(row)):
                x = len(__get_pattern(row[j], infinity))
                if not maxlen.has_key(j):
                    maxlen[j] = x
                else:
                    maxlen[j] = max(maxlen[j], x)
        for row in M:
            s = "[ "
            for j in xrange(len(row)):
                t = __get_pattern(row[j], infinity)
                for k in xrange(maxlen[j]-len(t)):
                    s += " "
                s += t + " "
            s += "]"
            print s

def __special_matrix_multiply(A, B, infinity):
    n, m = get_dimensions(A)
    C = create_matrix(n,m)
    for i in xrange(n):
        for j in xrange(m):
            C[i][j] = infinity
            for k in xrange(n):
                x = A[i][k] + B[k][j]
                if x < C[i][j]:
                    C[i][j] = x
    return C

def all_pairs_shortest_paths(matrix, infinity):
    n = get_num_rows(matrix)
    D = matrix
    m = 1
    while m < n-1:
        D = __special_matrix_multiply(D, D, infinity)
        m = 2 * m
    return D

vertices = [1,2,3,4]
edgeWeights = [(1,2,5), (2,3,1), (3,1,8), (3,4,3),(4,1,2)]

print "Given Data:"
print "Vertices =", vertices
print "Edge weights =", edgeWeights

# Determine safe infinity. Safe infinity equals sum of all weights + 1 
# or simplay assign python infinity value"
infinity = float("infinity")
n = len(vertices)

print "Weights in matrix format:"
matrix = create_matrix(n, n, infinity)
for (u,v,w) in edgeWeights:
    matrix[u-1][v-1] = w
for i in xrange(n):
    matrix[i][i] = 0
print_matrix(matrix, infinity)

print "Solution with repeated matrix multiplication"
D = all_pairs_shortest_paths(matrix, infinity)
print_matrix(D, infinity)
