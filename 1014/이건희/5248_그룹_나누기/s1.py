import sys
sys.stdin = open("input.txt")

def findset(x):
    if x == temps[x]:
        return x
    else:
        return findset(temps[x])

def union(a,b):
    temps[findset(a)] = findset(b)
    return

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    maps = list(map(int, input().split()))
    temps = [i for i in range(n + 1)]

    for i in range(m):
        union(maps[2*i], maps[2*i+1])

    for i in range(1,n+1):
        if temps[i] != i:
            temps[i] = findset(i)

    print("#{} {}".format(tc, len(set(temps[1:]))))
# Pass