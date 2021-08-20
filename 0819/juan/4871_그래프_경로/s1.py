import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]              # 인접 리스트 초기화

    for _ in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)                  # 인접한 정점 추가

    S, G = map(int, input().split())

    visited = [0] * (V+1)                       # 방문 체크 리스트 - 인덱스 편의상 V+1
    stack = [S]                                 # 출발 지점을 stack에 넣고 시작

    while stack:                                # stack이 빌 때까지 반복 (모든 정점 방문 완료)
        vertex = stack.pop()                    # 먼저 스택에서 정점을 하나 꺼내서
        if not visited[vertex]:                 # 그 정점이 방문하지 않은 정점이라면
            visited[vertex] = 1                 # 방문 처리 하고
            for v in adj[vertex]:               # 해당 정점에 연결된 다른 정점을 다시 반복하며
                if not visited[v]:           # 만약 그 곳이 방문하지 않은 곳이라면
                    stack.append(v)             # stack에 추가

    
    result = 1 if visited[G] else 0             # 도착지점의 방문 여부에 따라 1 또는 0 저장

    print('#{} {}'.format(tc, result))