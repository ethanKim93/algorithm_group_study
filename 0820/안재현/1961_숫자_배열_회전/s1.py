import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    box = [0] * (n * 3)

    for spin1 in range(n):
        temp = ''
        for i in range(n):
            temp += str(board[-1 - i][spin1])
        box[spin1 * 3] = temp

    for spin2 in range(n):
        temp1 = ''
        for j in range(n):
            temp1 += str(board[-1 - spin2][-1 - j])
        box[spin2 * 3 + 1] = temp1

    for spin3 in range(n):
        temp2 = ''
        for k in range(n):
            temp2 += str(board[k][-1 - spin3])
        box[spin3 * 3 + 2] = temp2

    print('#{}'.format(tc))
    for x in range(n * 3):
        if x % 3 == 2:
            print(box[x], end='')
            print()
        else:
            print(box[x], end=' ')