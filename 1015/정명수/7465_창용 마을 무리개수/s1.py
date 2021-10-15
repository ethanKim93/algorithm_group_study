import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x
def union(x,y):
    p[find_set(x)] = find_set(y)
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    p = list(range(N+1))
    for _ in range(M):
        a,b = map(int,input().split())
        union(a,b)
    cnt = 0
    for i in range(1,N+1):
        if i == p[i]:
            cnt += 1
    print('#{} {}'.format(tc,cnt))
