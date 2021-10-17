import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x != p[x]:
        x = find_set(p[x])
    return x


def union(a, b):
    p[find_set(b)] = find_set(a)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    price = []
    for i in range(N):
        for j in range(i, N):
            fee = ((X[i] - X[j])**2 + (Y[i]-Y[j])**2) * E  # L^2 * E
            price.append((fee, i, j))  # 가격순으로 정렬해야하기에 fee를 앞에 둔다.
    price.sort()
    p = [i for i in range(N)]
    min_p = 0
    for m in price:
        fee, i, j = m
        if find_set(i) != find_set(j):
            min_p += fee
            union(i, j)

    print('#{} {}'.format(tc, round(min_p)))