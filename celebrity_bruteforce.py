import random

# Find the first celebrity in a matrix of people. Celebrities know nobody
# Everyone knows the celebrity
def celebrity(matrix):
    n = len(matrix)
    # For all potential celebrities
    for i in range(n):
        eliminated = False
        # For every other person
        for j in range(n):
            if not eliminated:
                if i == j: # Same person
                    continue
                # If the possible celebrity knows someone, it's not a a celebrity
                # If somebody does not know the possible celebrity, its not a celebrity
                if matrix[i][j] or not matrix[j][i]:
                    eliminated = True
        if not eliminated:
            return i # If no breaks were encountered, we make it here and return the celeb

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
