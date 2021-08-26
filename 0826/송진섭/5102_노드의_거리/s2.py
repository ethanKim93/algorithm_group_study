# 인접행렬로 구현
import sys
sys.stdin = open('sample_input.txt')


def bfs(start, goal):
    visited = [0] * (V+1)
    q = [start]
    visited[start] = 1
    while q:
        t = q.pop(0)
        for i in range(1, len(adj)):
            if adj[t][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] + 1
    if not visited[goal] or not visited[start]:  # 둘 중 하나라도 0이면 간선이 이어지지 않은 것
        return 0
    else:
        return visited[goal] - visited[start]  # 노드간 거리 반환


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 생성
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    start, goal = map(int, input().split()) # 출발지, 목적지
    ans = bfs(start, goal)

    print('#{} {}'.format(tc, ans))