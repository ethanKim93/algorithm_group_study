import sys
sys.stdin = open('input.txt')
def bfs(s,e):
    visited = [0]*(V+1)
    q = [s]
    d = 1
    visited[s] = d
    while q:
        t = q.pop(0)
        for i in adj_list[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t]+1
    return visited[e]

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    way = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    adj_list = [[] for _ in range(V+1)]
    for i in way:
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    print('#{} '.format(tc),end='')
    if bfs(S,G):
        print(bfs(S,G)-1)
    else:
        print(0)






