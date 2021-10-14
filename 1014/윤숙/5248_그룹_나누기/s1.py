# 진석님 코드를 기반으로 이해하며 짜봤습니다.

import sys

sys.stdin = open('input.txt')
def find(x):
    if check[x]==x:
        return x
    else:
        return find(check[x])
def union(x,y):
    check[find(y)] = find(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) #사람수 #신청서
    numbers = list(map(int, input().split()))
    check = [i for i in range(N+1)] #조상표기
    for i in range(M):
        x, y = numbers[2 * i], numbers[2 * i + 1]
        union(x,y)
    print(check)
    for i in range(1, N + 1):
        if check[i] != i:
            check[i] = find(check[i])
    print(check)
    answer = len(set(check[1:]))
    print(answer)