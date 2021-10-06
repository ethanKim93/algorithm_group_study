# Runtime Error 코드
# 가지치기 필요!!

import sys
sys.stdin = open('sample_input.txt')


def perm(N):
    arr = list(range(1, N+1))
    used = [0]*(N)
    return_array = []

    def generate(pick, used):
        if len(pick) == N:
            return_array.append(pick[:])
            return

        for i in range(N):
            if used[i] != 1:
                pick.append(arr[i])
                used[i] = 1

                generate(pick, used)
                used[i] = 0
                pick.pop()

    generate([], used)
    return return_array


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    x = perm(N)
    ans = 999999999999
    for i in range(len(x)):
        e = 0
        for j in range(N-1):
            e += board[x[i][j]][x[i][j+1]]
        e += board[x[i][N-1]][x[i][0]]
        if e < ans:
            ans = e

    print('#{} {}'.format(tc, ans))