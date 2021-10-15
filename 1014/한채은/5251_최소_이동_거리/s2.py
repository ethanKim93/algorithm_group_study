import sys
sys.stdin = open('sample_input.txt')

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
def small_node():
    mini = INF
    # 가장 최단 거리가 짧은 노드(인덱스)
    idx = 0
    for i in range(1, n+1):
        if distance[i] < mini and not visited[i]:
            mini = distance[i]
            idx = i
    return idx

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = small_node()
        visited[now] = 1
        for j in graph[now]:
            cnt = distance[now] + j[1]
            if cnt < distance[j[0]]:
                distance[j[0]] = cnt

T = int(input())
for tc in range(1, T+1):

    INF = 9999999  # 무한을 의미(큰 수)

    # 마지막 연결지점 번호 n과 도로의 개수 e
    n, e = map(int, input().split())

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]

    # e개 줄에 걸쳐 구간 시작 s, 구간 끝 e, 구간 거리 w
    for _ in range(e):
        s, e, w = map(int, input().split())
        #  구간시작에서 끝으로가는 거리가 w
        graph[s].append((e, w))

    # 시작 노드 번호
    start = 0
    # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    visited = [0] * (n + 1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    dijkstra(start)

    print('#{} {}'.format(tc, distance[n]))
