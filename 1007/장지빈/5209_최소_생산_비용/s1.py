import sys
sys.stdin = open('input.txt')
from pprint import pprint

def check(row, newone):
    # if row == N:
    #     return newone
    # for i in range(N):
    #     for j in range(N):
    #         if not ai[i][j]:
    #             newone += V[i][j]
    #             ai[i][j] = 1
    # if row == N:
    #     return newone
    # min_cost = 100
    # for i in V[row]:
    #     if i < min_cost:
    #         min_cost = i
    # return min_cost
    # check(row+1, newone + min_cost)
    global ans, tmp
    if newone >= ans:
        return
    if row == N:
        if newone < ans:
            ans = newone
    for i in range(N):
        if not visited[i]:
            tmp += V[row][i]
            visited[i] = 1
            check(row+1, tmp)
            visited[i] = 0
            tmp -= V[row][i]


for tc in range(1, int(input())+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    # ai = [[0] * N] * N
    # pprint(V)
    ans = 100*16
    tmp = 0
    visited = [0]*N
    check(0, 0)
    # for i in range(N):
    #     ans += check(i, 0)
    print('#{} {}'.format(tc, ans))