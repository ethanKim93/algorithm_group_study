# Prim
import sys
sys.stdin = open("input.txt")

def prim(start):
    dist[start] = 0
    for _ in range(v):
        mn = inf
        for i in range(v+1):
            if not visited[i] and dist[i] < mn:
                mn = dist[i]
                mn_idx = i

        visited[mn_idx] = 1

        for x in range(1,v+1):
            if not visited[x] and maps[mn_idx][x]:
                if maps[mn_idx][x] < dist[x]:
                    dist[x] = maps[mn_idx][x]

    return sum(dist)

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    maps = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        s, g, w = map(int,input().split())
        maps[s][g], maps[g][s] = w, w

    inf = 99999
    dist = [inf] * (v+1)
    visited = [0] * (v+1)
    print("#{} {}".format(tc,prim(0)))

# Pass