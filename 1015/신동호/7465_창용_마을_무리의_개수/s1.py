import sys
sys.stdin = open('s_input.txt')

def find_set(x):
    if p[x] == x:
        return x
    else: 
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        if find_set(a) != find_set(b):
            union(a, b)

    ans = set()    
    for i in range(1, N+1):
        ans.add(find_set(i))


    print('#{} {}'.format(tc, len(ans)))