def rotate(matrix, n):
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the rows
    for i in range(n):
        matrix[i].reverse()


def matrix_input():
    rows = int(input("Enter number of rows: "))
    elements = int(input("Enter number of elements in each row: "))

    if rows != elements:
        return ValueError("No. of rows is not equal to no. of columns")

    matrix = []
    for i in range(rows):
        row_input = input(f"Enter elements of row {i+1}: ")
        row_elements = list(map(int, row_input.split()))
        matrix.append(row_elements)

    return matrix, rows


if __name__ == '__main__':
          
    # Matrix input
    matrix, size = matrix_input()
    print("Matrix before rotation:")
    for row in matrix:
        print(row)

    rotate(matrix, size)

    print("Matrix after rotation:")
    for row in matrix:
        print(row)
