import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    global p
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    pair = list(map(int, input().split()))
    for i in range(0, len(pair), 2):
        union(pair[i], pair[i+1])

    ans = set()
    for i in range(1, N+1):
        ans.add(find_set(i))
    print('#{} {}'.format(tc, len(ans)))