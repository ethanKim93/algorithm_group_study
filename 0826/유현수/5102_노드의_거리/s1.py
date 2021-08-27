import sys
sys.stdin = open('sample_input.txt')


def BFS(v):
    queue.append(v)
    visited[v] = 1
    while queue:
        curr = queue.pop(0)
        for w in adj_list[curr]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[curr] + 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    for i in range(E):
        adj_list[edge[i][0]].append(edge[i][1])
        adj_list[edge[i][1]].append(edge[i][0])

    queue = []
    visited = [0] * (V+1)
    BFS(S)
    if visited[G]:                                          # S와 G가 연결되어 있으면 거리 출력
        print('#{} {}'.format(tc, visited[G]-visited[S]))
    else:                                                   # 연결되어 있지 않으면 0 출력
        print('#{} 0'.format(tc))
