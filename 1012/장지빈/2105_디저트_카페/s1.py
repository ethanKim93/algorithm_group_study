import sys
from pprint import pprint
sys.stdin = open('input.txt')


dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dessert(i, j, k, n): # i: x좌표 / j: y좌표 / k: 방향(dx,dy) / n: cnt
    global si, sj, ans
    if k == 3 and i == si and j == sj:      # 3번 틀고 시작점에 도착한경우
        if ans < n:                         # cnt 비교
            ans = n
    elif i < 0 or i >= N or j < 0 or j >= N:# 범위 벗어나는지 여부 확인
        return
    elif cafe[i][j] in use:                 # 이미 방문한 곳 가면 return
        return
    else:
        use.append(cafe[i][j])              # use에 방문한 지점 추가

        if not k or k == 1:                 # 좌하 / 우하
            dessert(i+dx[k], j+dy[k], k, n+1)
            dessert(i+dx[k+1], j+dy[k+1], k+1, n+1)
        elif k == 2:                        # 좌상
            if i+j != si+sj:
                dessert(i+dx[2], j+dy[2], k, n+1)
            else:
                dessert(i + dx[3], j + dy[3], k+1, n + 1)
        else:   #k==3                       # 우상
            dessert(i+dx[3], j+dy[3], k, n+1)

        use.remove(cafe[i][j])
    return
for tc in range(1, int(input())+1):
    ans = -1
    N = int(input())    # 한 변의 길이
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    use = []
    for i in range(N):
        for j in range(1, N-1): #모서리 출발 불가
            si = i
            sj = j
            use.append(cafe[i][j])
            dessert(i+1, j+1, 0, 1)
            use.remove(cafe[i][j])

    print('#{} {}'.format(tc, ans))












# # direcnum 0: 하좌 / 1: 하우 / 2: 상우 / 3: 상좌
# def dessert(x, y, cnt, direc, direccnt):
#     global ans, visited, direction
#     if direc >= 4:
#         return
#     if direc == 3 and [x, y] == spoint:
#         if cnt > ans:
#             ans = cnt
#         return
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N and cafe[x][y] != cafe[nx][ny] and not visited:
#             visited[nx][ny] = 1
#             try:
#
#             dessert(nx, ny, cnt, direction, direccnt)
#             visited[nx][ny] = 0
#     return
#
# for tc in range(1, int(input())+1):
#     ans = -1
#     N = int(input())    # 한 변의 길이
#     cafe = [list(map(int, input().split())) for _ in range(N)]
#     # pprint(cafe)
#     visited = [[0]*N for _ in range(N)]
#     direction = []
#     for i in range(N):
#         for j in range(1, N-1): #모서리 출발 불가
#             spoint = [i, j]
#             dessert(i, j, 1, 0, 0)
#
#     print('#{} {}'.format(tc, ans))