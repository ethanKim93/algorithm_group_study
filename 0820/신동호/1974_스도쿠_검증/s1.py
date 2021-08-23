import sys
sys.stdin = open('input.txt')

T = int(input())

def check(sudoku):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            if row[sudoku[i][j]]:
                return 0
            else:
                row[sudoku[i][j]] = 1
            if col[sudoku[j][i]]:
                return 0
            else:
                col[sudoku[j][i]] = 1

            if not (i%3 or j%3):
                box = [0] * 10
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if box[sudoku[x][y]]:
                            return 0
                        else:
                            box[sudoku[x][y]] = 1
    return 1
for tc in range(1, T+1):
    sud = [list(map(int,input().split())) for _ in range(9)]
    print('#{} {}'.format(tc,check(sud)))