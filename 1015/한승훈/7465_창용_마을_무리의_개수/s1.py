import sys
sys.stdin = open('s_input.txt')


def find_set(a):
    while a != p[a]:
        a = p[a]
    return a


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    for _ in range(M):
        s1, s2 = map(int, input().split())
        p[find_set(s2)] = find_set(s1)
    for j in range(N+1):
        p[j] = find_set(j)
    p = set(p)
    cnt = len(p)-1
    print('#{} {}'.format(tc, cnt))