import sys

sys.stdin = open("input.txt")


def find(start):
    visited = [0] * n
    dist = [inf] * n
    dist[start] = 0
    for _ in range(n):
        mn = inf
        for i in range(n):
            if dist[i] < mn and not visited[i]:
                mn = dist[i]
                mn_idx = i

        visited[mn_idx] = 1

        for i in range(n):
            if temps[mn_idx][i] and not visited[i]:
                if temps[mn_idx][i] < dist[i]:
                    dist[i] = temps[mn_idx][i]
    return sum(dist)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = []
    maps_x = list(map(int, input().split()))
    maps_y = list(map(int, input().split()))
    for i in range(n):
        maps.append([maps_x[i], maps_y[i]])
    e = float(input())

    temps = [[0] * n for _ in range(n)]
    inf = 9876543210000
    for i in range(n):
        for x in range(n):
            temps[i][x] = (maps[i][0] - maps[x][0]) ** 2 + (maps[i][1] - maps[x][1]) ** 2

    print("#{} {}".format(tc, round(find(0) * e)))
# Pass