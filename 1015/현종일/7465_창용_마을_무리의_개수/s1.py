import sys
sys.stdin = open("s_input.txt")

def findset(x):
    if x == leaders[x]:
        return x
    else:
        return findset(leaders[x])

def union(x,y):
    leaders[findset(y)] = findset(x)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    knowns = [list(map(int, input().split())) for _ in range(M)]
    leaders = [i for i in range(N+1)]

    for known in knowns:
        p1, p2 = known
        union(p1, p2)

    for i in range(1, N+1):
        leaders[i] = findset(i)

    leaders.pop(0)
    print("#{} {}".format(tc, len(set(leaders))))


