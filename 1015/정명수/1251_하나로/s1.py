import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != p[x]:
        x=p[x]
    return x
def union(x,y):
    p[find_set(x)] = find_set(y)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x_s = list(map(int,input().split()))
    y_s = list(map(int,input().split()))
    cost = float(input())
    edges = []
    for i in range(N):
        for j in range(i+1,N):
            dist = (x_s[i]-x_s[j])**2 + (y_s[i]-y_s[j])**2
            edges.append((dist,i,j))
    edges.sort()
    idx = 0
    p = list(range(N+1))
    ans = 0
    cnt = 1
    while cnt<N:
        n1=edges[idx][1]
        n2=edges[idx][2]
        if find_set(n1) != find_set(n2):
            union(n1,n2)
            ans += edges[idx][0]
            cnt += 1
        idx += 1
    print('#{} {}'.format(tc,round(ans*cost)))