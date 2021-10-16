import sys
sys.stdin = open('sample_input.txt')

def find_set(n):
    while p[n] != n:
        n = p[n]
    return n

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    li = list(map(int,input().split()))
    p = [i for i in range(N+1)]
    for i in range(M):
        a1, a2 = li[i*2], li[i*2+1]
        p[find_set(a1)] = find_set(a2)
    cnt = 0
    for k in range(1,N+1):
        n = find_set(k)
        if n == k:
            cnt += 1
    print('#{} {}'.format(tc,cnt))



# dfs

def dfs(n):
    visited[n] = 1
    res.append(n)
    for w in arrList[n]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)
        else:
            for k in result:
                if w in k:
                    k.append(n)
                    res.clear()

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    li = list(map(int,input().split()))
    arrList = [[] for _ in range(N+1)]
    check = set()
    for i in range(M):
        a1, a2 = li[i*2], li[i*2+1]
        arrList[a1].append(a2)
        arrList[a2].append(a1)
        check.add(a1)
        check.add(a2)
    visited = [0] * (N + 1)
    cnt = N - len(check)
    result = []
    for k in check:
        if visited[k] : continue
        res = []
        dfs(k)
        if res:
            result.append(res)
    print('#{} {}'.format(tc,cnt+len(result)))