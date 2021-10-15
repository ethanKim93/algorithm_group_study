import sys
sys.stdin = open('s_input.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    for _ in range(M):
        a, b = map(int, input().split())
        p[find_set(b)] = find_set(a)

    for i in range(1, N+1):
        p[i] = find_set(i)
    
    print('#{} {}'.format(tc, len(set(p[1:]))))
