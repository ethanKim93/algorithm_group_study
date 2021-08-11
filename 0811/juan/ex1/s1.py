import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # pprint(arr)

    total = 0
    for i in range(N):
        for j in range(N):
            part = 0
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    now = arr[nr][nc] - arr[i][j]
                    if now < 0:
                        now *= -1
                    part += now
            total += part
    print(total)