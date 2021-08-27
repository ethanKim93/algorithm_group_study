import sys
sys.stdin = open('sample_input.txt')


def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in range(1, V+1):  # 다음에 갈 노드들
            if not visited[i] and node[t][i]:
                queue.append(i)
                visited[i] = visited[t] + 1
                if i == G:  # 다음에 갈 노드가 도착지점인지 확인
                    return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        e1, e2 = map(int, input().split())
        node[e1][e2] = node[e2][e1] = 1
    S, G = map(int, input().split())
    bfs(S)
    if visited[G]:
        ans = visited[G]-1
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))
