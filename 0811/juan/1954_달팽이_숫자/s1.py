import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    dir = 0
    r, c = 0, -1
    cnt = 1

    while cnt <= N*N:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
            arr[nr][nc] = cnt
            cnt += 1
            r, c = nr, nc
        else:
            dir = (dir + 1)%4
    pprint(arr)


# for tc in range(1, T+1):
#     N = int(input())

#     arr = [[0] * N for _ in range(N)]
#     arr[0][0] = 1
    
#     r, c = 0, 0
#     n = 1
    
#     while n < N*N:
#         for i in range(4):
#             r += dr[i]
#             c += dc[i]
    
#             while (0 <= r < N and 0 <= c < N) and not arr[r][c]:
#                 n += 1
#                 arr[r][c] = n
    
#                 r += dr[i]
#                 c += dc[i]
#             r -= dr[i]
#             c -= dc[i]
#     print('#{}'.format(tc))
#     for row in arr:
#         print(*row)