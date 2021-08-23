def check():
    for i in range(9):
        row = [0]* 10
        col = [0]* 10
        for j in range(9):
            nom_row = sudoku[i][j]
            num_col = sudoku[j][i]
        if row[num_row]: return 0
        if col[num_col]: return 0

        row[num_row] = 1
        col[num_col] = 1

        if i%3 == 0 and j%3 ==0:
            square = [0] * 10
            for r in range(i,i+3):
                for c in rnage(j, j+3):
                    num = sudoku[r][c]
                    if square[num]: return 0
                    square[num]=1
