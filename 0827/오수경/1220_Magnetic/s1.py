import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    crush = []
    result = 0


    for i in range(N):
        for j in range(N):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in range(N):
        for j in board[i]:
            if j == 1 and len(crush) == 0:
                crush.append(j)
            elif j == 2:
                if len(crush) == 0:
                    continue
                else:
                    crush.pop()
                    result += 1
        crush = []

    print('#{} {}'.format(tc, result))