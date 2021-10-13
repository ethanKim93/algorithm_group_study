import sys
import copy
from collections import deque
sys.stdin = open("input.txt")

def check(maps):
    cnt = 0
    for i in range(r):
        for x in range(c):
            if maps[i][x] != 0:
                cnt += 1
    return cnt

def BFS(idy, maps):
    maps = copy.deepcopy(maps)
    for i in range(r):
        if maps[i][idy] != 0:
            start_idx, start_idy = i, idy
            break
    else:
        return maps

    q = deque()
    q.append([start_idx, start_idy])
    while q:
        now_r, now_c = q.popleft()
        for i in range(maps[now_r][now_c]):
            for x in range(4):
                nr = now_r + dirs[x][0] * i
                nc = now_c + dirs[x][1] * i
                if 0 <= nr < r and 0 <= nc < c:
                    if maps[nr][nc] != 0:
                        q.append([nr, nc])
        maps[now_r][now_c] = 0
    return maps

def MOVE(maps):
    maps = copy.deepcopy(maps)
    for i in range(c):
        for x in range(r - 1, 0, -1):
            if maps[x][i] == 0:
                for y in range(x - 1, -1, -1):
                    if maps[y][i] != 0:
                        maps[x][i], maps[y][i] = maps[y][i], maps[x][i]
                        break
    return maps

def BF(cnt, maps):
    global ans
    if cnt == n:
        now_cnt = check(maps)
        if ans > now_cnt:
            ans = now_cnt
        return

    for i in range(c):
        if temps[i] <= n:
            temps[i] += 1
            BF(cnt + 1, MOVE(BFS(i, maps)))
            temps[i] -= 1


t = int(input())
for tc in range(1, t + 1):
    n, c, r = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(r)]
    temps = [0] * c
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ans = 180
    BF(0, maps)
    print("#{} {}".format(tc, ans))
