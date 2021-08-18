# 교수님 코드를 변형해서 작성해보기!

import sys
sys.stdin = open('input.txt')

def is_pal(x):                          # 회문 여부 재귀로 확인
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return True

def check(board, N=100, M=100):
    while M > 1:
        for i in range(N):
            for j in range(N-M+1):
                row = ''                    # 행방향 문자열 저장할 변수 초기화
                col = ''                    # 열방향 문자열 저장할 변수 초기화
                for k in range(M):
                    row += board[i][j+k]    # 행방향으로 길이 M 만큼의 문자열 concatenate
                    col += board[j+k][i]    # 열방향으로 길이 M 만큼의 문자열 concatenate
                if is_pal(row):             # row가 회문이면
                    return len(row)         # row length return
                if is_pal(col):             # col이 회문이면
                    return len(col)         # col length return
        M -= 1

for _ in range(10):
    test = int(input())
    board = [list(input()) for _ in range(100)]
    result = check(board)


    print('#{} {}'.format(test, result))
