def displayMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(0, row):
        for j in range(0, col):
            print(matrix[i][j], end=" ")
        print()

def isSafe(mat, i, j, no) -> bool:
    # check along the rows and columns simultaneously
    for k in range(0, 9):
        if (mat[i][k] == no or mat[k][j] == no):
            return False

    # Check in the subgrid
    temp_i = int(i/3) * 3;
    temp_j = int(j/3) * 3;
    for di in range(temp_i, temp_i+3):
        for dj in range(temp_j, temp_j+3):
            if (mat[di][dj] == no):
                return False

    return True

def sudokuSolver(mat, i, j) -> bool:
    row = len(mat)
    col = len(mat[0])

    # base case
    if (i == row):
        displayMatrix(mat)
        return True

    # recursive case
    if (j == col):
        return sudokuSolver(mat, i+1, 0)

    if (mat[i][j] != 0):
        return sudokuSolver(mat, i, j+1)

    for no in range(1, 10):
        if (isSafe(mat, i, j, no)):
            mat[i][j] = no
            isSolved = sudokuSolver(mat, i, j+1)
            if (isSolved):
                return True

    mat[i][j] = 0
    return False

def main():
    mat = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    if sudokuSolver(mat, 0, 0) == False:
        print("No solution exists!")


if __name__ == "__main__":
    main()
