import random
# This problem can be reduced by the fact that
# if matrix[u][v], then we know u is not a celebrity,
# if not matrix[u][v], then we know that v is not a celebrity
# This means we can start eliminating these non celebrities
# In a conveyer belt
def celebrity(matrix):
    n = len(matrix)
    # The first two people, we begin eliminating
    u, v = 0, 1
    for i in range(2, n + 1):
        # u knows someone, not a celeb
        if matrix[u][v]:
            u = i
        # v is not known, not a
        else:
            v = i

    # As we iterated above, someone was always getting replaced/eliminated as
    # not a celeb, the last person to get eliminated is obviously not a celeb,
    # so the person besides from the last person (we're keeping track of 2 people)
    # has a chance of being a celebrity, if at least one exists actually.
    celeb = None
    if u == n:
        celeb = v
    else:
        celeb = u
    eliminated = False
    for person in range(n):
        if person == celeb:
            continue
        if matrix[celeb][person] or not matrix[person][celeb]:
            eliminated = True
    if not eliminated:
        return celeb
    return None

def main():
    matrix = [[random.randint(0, 1)]*5 for i in range(5)]
    for i in range(random.randint(0, len(matrix) - 1)):
        for j in range(len(matrix)):
            matrix[j][i] = 1
            matrix[i][j] = 0
    for i in range(len(matrix)):
        print matrix[i]
    celeb = celebrity(matrix)
    print "Celebrity:", celeb

if __name__ == "__main__":
    main()
