import sys
sys.stdin = open("input.txt")

def findset(x):
    if x == maps[x]:
        return x
    else:
        return findset(maps[x])

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    maps = [i for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        if findset(a) != findset(b):
            maps[findset(b)] = findset(a)

    for i in range(1, n + 1):
        maps[i] = findset(i)

    print("#{} {}".format(tc, len(set(maps[1:]))))

# Pass