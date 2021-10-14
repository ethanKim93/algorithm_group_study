# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지

# 라이브에서 했던 방식 1번으로 함

import sys
sys.stdin = open('input.txt', 'r')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):  # r,c: 현재 위치
    ir = r
    ic = c
    for i in range(4):
        nr = ir + dr[i]
        nc = ic + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if room[r][c] + 1 == room[nr][nc]:
                roomli[room[r][c]] = 1
                return
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    roomli = [0 for _ in range(N**2+1)]
    for i in range(N):
        for j in range(N):
            dfs(i, j)

    ans = 0  # 연속된 1의 최대 길이
    idx = -1

    flag = 0
    for k in range(N**2, -1, -1):  # 0까지 돌아야 1번까지 연속되었던 1을 ans에 반영할 수 있음!!
        if flag <= 0:
            if roomli[k] == 1:
                flag = 1
        else:
            if roomli[k] == 1:
                flag += 1
            else:
                if flag+1 >= ans:
                    ans = flag+1
                    idx = k+1
                flag = 0
    print('#{} {} {}'.format(tc, idx, ans))


#####################################################################################
# 일반 dps로 풀음 -> RecursionError: maximum recursion depth exceeded in comparison
# <= N최대 1000이라서 연산이 너무 많이 들어감.

# 방의 숫자는 모두 다르고 이동하려면 현재 방에 적힌 숫자보다 정확히 1 더 커야 하므로
# -> visited 기록 필요 없을듯

# import sys
# sys.stdin = open('input.txt', 'r')
#
# # 우하좌상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# def dfs(r, c, cnt):  # r,c: 현재 위치 / cnt: 이동한 방의 개수
#     global ans, roomN
#
#     ir = r
#     ic = c
#     for i in range(4):
#         nr = ir + dr[i]
#         nc = ic + dc[i]
#         if 0 <= nr < N and 0 <= nc < N:
#             if room[r][c] + 1 == room[nr][nc]:
#                 dfs(nr, nc, cnt+1)
#
#     if ans < cnt:
#         ans = cnt
#         roomN.append(room[n][m])
#     return
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     roomN = []
#     for n in range(N):
#         for m in range(N):
#             dfs(n, m, 0)
#     print(min(roomN), ans+1)
