T = int(input())

for case in range(T):
    sudoku = [[0]] * 9
    check = 1

    for r in range(9):
        sudoku[r] = list(map(int, input().split()))
        if len(set(sudoku[r])) != 9:  # 넣으면서 가로 확인
            check = 0

    if check:
        for col in range(9):
            set_col = set()
            for row in range(9):
                set_col.add(sudoku[row][col])  # 세로 확인
                if not row % 3 and not col % 3:
                    set_3by3 = set()
                    for i in range(row, row + 3):
                        for j in range(col, col + 3):
                            set_3by3.add(sudoku[i][j])  # 3*3 확인
                    if len(set_3by3) != 9:
                        check = 0
                        break
            if len(set_col) != 9 or not check:
                check = 0
                break

    print(f"#{case + 1} {check}")