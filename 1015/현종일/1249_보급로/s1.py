import sys
sys.stdin = open("input.txt")
from collections import deque

dc = [0, 1, 0, -1] # 우 하 좌 상
dr = [1, 0, -1, 0]

def bfs():
    queue = deque()
    queue.append((0, 0))
    while queue:
        c, r = queue.popleft()
        for arrow in range(4):
            nc = c + dc[arrow]
            nr = r + dr[arrow]
            if 0 <= nc < N and 0 <= nr < N:
                if costs[c][r] + field[nc][nr] < costs[nc][nr]:
                    costs[nc][nr] = costs[c][r] + field[nc][nr]
                    queue.append((nc, nr))



for tc in range(1, int(input())+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]
    costs = [[987654321] * N for i in range(N)]
    costs[0][0] = 0
    bfs()
    print("#{} {}".format(tc, costs[N-1][N-1]))


