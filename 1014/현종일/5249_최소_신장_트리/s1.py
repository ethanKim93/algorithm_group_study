import sys
sys.stdin = open("sample_input.txt")

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(x)] = find_set(y)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    p = [i for i in range(V+1)]

    result = 0
    cnt = 0
    for n1, n2, w in edges:
        if cnt == V:
            break
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            result += w
            cnt += 1

    print("#{} {}".format(tc, result))