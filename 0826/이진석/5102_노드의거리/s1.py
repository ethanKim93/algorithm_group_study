import sys
sys.stdin = open('sample_input.txt')

def BFS(start,goal):
    q = [start]                                 # queue 초기화.
    visited[start] = 1                          # 시작 노드 방문 표시
    while q:                                    # queue 가 비면 종료
        v = q.pop(0)                            # 현재 노드
        for w in range(1, V+1):
            if node[v][w] and not visited[w]:   # 현재 노드와 연결된 노드 중 방문 안한 노드 일 때
                q.append(w)                     # enQ(다음 노드)
                visited[w] = 1                  # 다음 노드 방문표시
                road[w] = road[v] + 1           # start 노드와의 거리 갱신(현재 노드와 연결되어 있다는 뜻이므로 1 추가)
                if w == goal:                   # 다음 노드가 목표 노드라면 BFS 종료
                    return road[w]
    return 0                                    # queue가 비는 순간까지 목표 노드를 찾지 못했다면 0 반환

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    node = [[0] * (V+1) for _ in range(V+1)]    # 노드 정보 초기화
    road = [0] * (V+1)                          # start 노드와 각 노드와의 거리
    visited = [0] * (V+1)                       # 방문표시 초기화

    for _ in range(E):                          # 노드 정보 입력
        e1, e2 = map(int,input().split())
        node[e1][e2] = node[e2][e1] = 1                        # 양방향 노드

    s, g = map(int, input().split())            # 시작지점, 도착지점 입력
    print('#{} {}'.format(tc, BFS(s,g)))
