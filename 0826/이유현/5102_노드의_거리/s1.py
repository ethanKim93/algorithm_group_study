import sys
sys.stdin = open('sample_input.txt')


def bfs(start):
    visited = [0] * (V + 1)
    q = []					    # 큐 생성
    q.append(start)				# 시작점 인큐
    visited[start] = 1			# 시작점 visited 표시
    while q:					# 큐가 비어있지않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)			# 디큐 (꺼내서)해서 t에 저장

        for i in range(1, V+1):	# t에 인접이고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)						# enqueue(i)
                visited[i] = visited[t] + 1		# i visited로 표시
    return visited


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        edge.append(list(map(int, input().split())))

    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for e in edge:
        n1, n2 = e[0], e[1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    S, G = map(int, input().split())
    result = bfs(S)[G] - 1
    if result < 0:
        result = 0

    print('#{} {}'.format(tc, result))
