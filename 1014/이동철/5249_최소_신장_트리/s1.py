import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # V 는 마지막 노드번호, E 는 간선 개수

    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    # 노드와 가중치 표현을 위한 2차원 list
    for _ in range(E):
        node_1, node_2, w = map(int, input().split())
        graph[node_1][node_2] = graph[node_2][node_1] = w

    num = 987654321
    visited = [0] * (V + 1)
    # 모든 정점은 한 번씩만 방문해야하기 때문에
    # 방문표시를 위한 visited 리스트를 생성
    result = [num] * (V + 1)
    # 이미 방문한 노드 중 인접한 노드에서 가장 적은 가중치의 노드를 찾기 위한 result

    start_node = 0
    visited[start_node] = 1
    result[start_node] = 0
    connected = 0

    while connected < V:
        # V-1개가 될 때까지 정점들을 연결
        for next_node in range(V + 1):
            # 처음 for 문은 바로 이전에 선택했던 정점과 연결된 정점을 선택
            if not visited[next_node] and graph[start_node][next_node] \
                    and graph[start_node][next_node] < result[next_node]:
                result[next_node] = graph[start_node][next_node]
                # 이를 통해 아직 방문하지않은 정점 중들의 최솟값을 갱신
                # 지금까지 선택한 정점과 인접한 정점들의 최솟값이 result 에 있다.

        min_w = num
        for next_node in range(V + 1):
            # 두 번째 for 문은 result 를 통해 지금까지 방문한 노드에서
            # 인접한 노드 중 최솟값을 갖는 노드를 선택
            if not visited[next_node] and result[next_node] < min_w:
                min_w = result[next_node]
                start_node = next_node

        visited[start_node] = 1
        connected += 1

    answer = sum(result)
    print("#{} {}".format(tc, answer))



