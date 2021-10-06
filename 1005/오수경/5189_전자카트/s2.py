# pass 코드

import sys
sys.stdin = open('sample_input.txt')


def energy(x):
    global ans, N
    e = 0
    for j in range(len(x)-1):
        e += board[x[j]][x[j+1]]

    if len(x) == N:
        e += board[x[N-1]][x[0]]
        if e < ans:
            ans = e
    return e


def perm(N):
    global ans
    arr = list(range(1, N+1))
    used = [0]*N


    def generate(pick, used):
        if len(pick) == N:
            energy(pick[:])
            return

        elif energy(pick) > ans:
            return

        for i in range(N):
            if used[i] != 1:
                pick.append(arr[i])
                used[i] = 1

                generate(pick, used)
                used[i] = 0
                pick.pop()

    generate([], used)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    ans = 999999999
    x = perm(N)

    print('#{} {}'.format(tc, ans))