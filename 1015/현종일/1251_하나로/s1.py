import sys
sys.stdin = open("input.txt")

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    N = int(input())
    p = [i for i in range(N)]
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    tax = float(input())

    field = []
    for i in range(N):
        for j in range(i+1, N):
            cost = (x[i] - x[j])**2 + (y[i] - y[j])**2
            field.append([i, j, cost])

    field.sort(key=lambda x: x[2])

    result = 0
    cnt = 0
    for x, w, c in field:
        if cnt == N:
            break

        if find_set(x) != find_set(w):
            cnt += 1
            result += c
            union(x, w)

    print('#{} {}'.format(tc, round(result*tax)))