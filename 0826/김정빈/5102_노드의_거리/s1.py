import sys
sys.stdin = open("input.txt")

def bfs(s, g):
    q = [s]
    visited = [0]*(V+1)
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in adj_list[t]:
            if visited[i] == 0:
                if i == g:
                    return visited[t]
                else:
                    q.append(i)
                    visited[i] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    s,g = map(int,input().split())

    #인접리스트
    adj_list = [[]*V for _ in range(V+1)]
    for i in range(E):
        n1, n2 = node[i][0], node[i][1]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    print('#{} {}'.format(tc, bfs(s,g)))