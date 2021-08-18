import sys
sys.stdin = open('input.txt')


def is_pal(x):                          # 회문 여부 재귀로 확인
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return True


def check(board, N, M):
    for i in range(N):
        for j in range(N-M+1):
            row = ''                    # 행방향 문자열 저장할 변수 초기화
            col = ''                    # 열방향 문자열 저장할 변수 초기화
            for k in range(M):
                row += board[i][j+k]    # 행방향으로 길이 M 만큼의 문자열 concatenate
                col += board[j+k][i]    # 열방향으로 길이 M 만큼의 문자열 concatenate
            if is_pal(row):             # row가 회문이면
                return M                # row return
            if is_pal(col):             # col이 회문이면
                return M                # col return]
    return 0


for tc in range(1, 11):
    testCase = int(input())
    board = [list(input()) for _ in range(100)]
    lenSet = set()
    for num in range(1, 101):
        lenSet.add(check(board, 100, num))
    maxV = 1
    for key in lenSet:
        if key > maxV:
            maxV = key
    print('#{} {}'.format(tc, maxV))



'''
# 내가 하다 망함

import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    testCase = int(input())
    board = [list(input()) for _ in range(100)]
    lenSet = set()

    for row in range(100):
        for i in range(1, 50):
            if board[row][i] == board[row][i+1]:

            for plus in range(1, i+1):
                if board[row][i-plus] != board[row][i+plus]:
                    lenSet.add(1 + 2*plus-2)
                    break
        for i in range(50, 99):
            for plus in range(1, 100-i):
                if board[row][i-plus] != board[row][i+plus]:
                    lenSet.add(1 + 2*plus-2)
                    break
    print(lenSet)
    maxV = 1
    for key in lenSet:
        if key > maxV:
            maxV = key

    print('#{} {}'.format(tc, maxV))
'''
