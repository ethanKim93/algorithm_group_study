
import sys
sys.stdin = open("input.txt")

T = int(input())

def road(x, y, total):
    global result
    if x == N-1 and y == N-1:
        total += arr[y][x]
        if total < result:
            result = total
            return
    if total > result:
        return

    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        x += dx[i]
        y += dy[i]
        if x > N-1 or y > N-1:
            continue
        if not visited[y][x]:
            visited[y][x] = 1
            road(cx, cy, total + arr[y][x])
            visited[y][x] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    temp = 0
    result = 10 * 2 * N
    visited = [[0 for _ in range(N)]for _ in range(N)]
    road(0, 0, 0)


    print("#{} {}".format(tc, result))