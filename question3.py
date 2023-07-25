#question3.py --> Defining longest increasing path

def longest_path(matrix):
    if not matrix:
        return 0

    i, j = len(matrix), len(matrix[0])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dir_search(row, column, a):
        if (row, column) in a:
            return a[(row, column)]

        path = 1
        for rowdir, coldir in direction:
            new_row, new_column = row + rowdir, column + coldir
            if 0 <= new_row < i and 0 <= new_column < j and matrix[new_row][new_column] > matrix[row][column]:
                path = max(path, 1 + dir_search(new_row, new_column, a))

        a[(row, column)] = path
        return path

    max_long = 0
    a = {}
    for b in range(i):
        for c in range(j):
            max_long = max(max_long, dir_search(b, c, a))

    return max_long

# Testing the code
matrix = [[8,7,4],[4,4,8],[2,1,0]]
result = longest_path(matrix)
print(result)
