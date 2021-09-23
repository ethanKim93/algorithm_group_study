import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if board[j][i] == 1:
                stack.append(1)
            elif stack and stack[-1] == 1 and board[j][i] == 2:
                stack.append(2)
                cnt += 1
    print('#{} {}'.format(tc, cnt))



