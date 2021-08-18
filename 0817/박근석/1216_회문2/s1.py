import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    num = input()
    board = [list(input()) for _ in range(100)]

    max_num = 0

    for i in range(100):
        for j in range(100):
            for k in range(j+1):
                row = ''
                col = ''
                for l in range(k,k+(100-j)):
                    row += board[i][l]
                    col += board[l][i]
                if row == row[::-1]:
                    if max_num < len(row):
                        max_num = len(row)
                if col == col[::-1]:
                    if max_num < len(col):
                        max_num = len(col)

    print('#{} {}'.format(num, max_num))



