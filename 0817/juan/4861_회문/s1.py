import sys
sys.stdin = open('sample_input.txt')

T = int(input())

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
                return row              # row return
            if is_pal(col):             # col이 회문이면
                return col              # col return

for tc in range(1, T+1):
    N,M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, check(board, N, M)))
