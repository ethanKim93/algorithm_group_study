import sys
sys.studin = open('sample_input.txt','r')

def dfs(idx,cnt):
    global max_v
    visit[idx] = True
    if cnt > max_v:
        max_v = cnt
    for i in s[idx]:
        if visit[i]:
            dfs(i,cnt+1)
            visit[i] = 0

for tc in range(int(input())):
    n,m = map(int,input().split())
    s=[[] for i in range(n+1)]
    for i in range(m):
        x,y = map(int,input().split())
        s[x].append(y)
        s[y].append(x)
    max_v = 0

    for i in range(1,n+1):
        visit = [0] * (n+1)
        dfs(i,1)
    print('#{} {}'.format(tc,max_v))