# 못풂

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):

    print('#{} {}'.format(tc, result))


# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(arr)
#     blank = []
#     idx = 0
#
#     # 행 순회
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 try:
#                     blank[idx] += 1
#                 except:
#                     blank.append(1)
#             if not arr[i][j]:
#                 idx = len(blank)
#         if arr[i][N-1]:
#             pass
#         idx += 1
#     idx += 1
#
#     # 열 순회
#     for j in range(N):
#         for i in range(N):
#             if arr[i][j]:
#                 try:
#                     blank[idx] += 1
#                 except:
#                     blank.append(1)
#             if not arr[i][j]:
#                 idx = len(blank)
#         idx += 1
#
#     result = 0
#     for num in blank:
#         if num == K:
#             result += 1
#
#     print(blank)
#
#     print('#{} {}'.format(tc, result))

