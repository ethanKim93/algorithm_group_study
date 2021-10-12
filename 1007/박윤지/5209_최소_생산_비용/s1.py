# 사람들 코드 참고해서 품
# dfs

import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(start, total):  # total을 들고다녀야 시간초과 안남
    global ans
    if total >= ans:
        return

    if start == N:
        if total < ans:
            ans = total

    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(start+1, total + cost[start][i])
            visited[i] = 0  # 지났던 거 다시 취소


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 99*15
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))

########################################################
# # 순열 먼저 만들고 최솟값인지 확인함. 시간초과 망함
# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# def perm(n, k):
#     if n == k:
#         global ans
#         cnt = 0
#         for j in range(0, N):
#             cnt += cost[j][arr[j]]
#             if cnt > ans:
#                 return
#         if cnt < ans:
#             ans = cnt
#     else:
#         for i in range(k, n):
#             arr[i], arr[k] = arr[k], arr[i]
#             perm(n, k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     cost = [list(map(int, input().split())) for _ in range(N)]
#     # 0부터 N-1까지 순열 만들기
#     arr = list(range(N))
#     ans = 99*15
#     perm(N, 0)
#     print('#{} {}'.format(tc, ans))