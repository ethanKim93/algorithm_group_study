# Kruskal
import sys
sys.stdin = open("input.txt")

def findset(x):
    if temps[x] == x:
        return x
    else:
        return findset(temps[x])

def union(a,b):
    a, b = findset(a), findset(b)
    if a < b:
        temps[b] = a
    else:
        temps[a] = b

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    maps = []
    for i in range(m):
        s, g, value = map(int,input().split())
        maps.append([s, g, value])

    maps = sorted(maps, key= lambda x: x[2])

    temps = [i for i in range(n+1)]
    ans = 0
    for s, g, value in maps:
        if findset(s) != findset(g):
           ans += value
           union(s,g)

    print("#{} {}".format(tc,ans))

# Pass