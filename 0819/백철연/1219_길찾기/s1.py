
# 인접리스트 DFS
import sys
sys.stdin = open('input.txt')

for tc in range(10):
    t, E = map(int, input().split())

    lis = [[] for _ in range(100)] # 빈 리스트 생성
    edge_input = list(map(int, input().split()))

    # 화살표 있으면 1로 변경
    for i in range(E):
        start_node = edge_input[i * 2]
        end_node = edge_input[i * 2 + 1]
        lis[start_node].append(end_node)

    visited = [0] * 100
    stack = [0]

    while stack:  # stack이 빌 때 까지 반복.
        now = stack.pop()  # 나의 현재위치(현재 있는 노드)

        if not visited[now]:  # 아직 방문 안했으면
            visited[now] = True  # 방문

            for v in lis[now]:
                if not visited[v]:
                    stack.append(v)

    # 99번에 방문했다면 1 출력, 방문 못했으면 0 출력
    result = 1 if visited[99] else 0
    print("#{} {}".format(t, result))