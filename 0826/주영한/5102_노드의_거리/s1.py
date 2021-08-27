import sys
sys.stdin = open("sample_input.txt")


def BFS(connection_list, start, end):

    # 노드의 갯수 + 1이 num_nodes이다. 인덱스와 노드 번호간
    # 연산을 간단하게 하기 위하여 +1을 해주었다.
    num_nodes = len(connection_list)
    visited = [0] * num_nodes

    # 방문할 노드의 순서를 나타내는 queue를 생성한다.
    queue = [0] * num_nodes

    # 선형 큐의 형태로 front와 rear를 설정한다.
    # 이때 초기 상태에 시작점이 들어가 있으므로,
    # visited와 front, rear를 설정한다.
    queue_front = -1
    queue_rear = 0
    queue[queue_rear] = start
    visited[start] = 1


    # 큐가 빌때까지 진행한다.
    while queue_rear - queue_front:
        # deQueue에 대한 연산을 실행한다.
        queue_front += 1
        temp_node = queue[queue_front]

        # dequeue 해준 노드와 연결된 노드 중 방문하지 않은 노드를
        # 큐에 넣어주고, 이때 dequeue 해준 노드로 부터 한 칸 떨어져 있으므로
        # visited[target] = visited[temp_node] + 1로 업데이트 해준다.
        for target in connection_list[temp_node]:
            if not visited[target]:
                queue_rear += 1
                queue[queue_rear] = target
                visited[target] = visited[temp_node] + 1

    # 연결되어 있을 경우, 시작점이 1부터 시작하였으므로 1을 빼어 반환해주고,
    # 연결되어 있지 않을경우, 그대로 0을 출력한다.
    return visited[end] - 1 if visited[end] else visited[end]

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    connection_list = [[] for _ in range(V + 1)]
    for connect in range(E):
        con_start, con_end = map(int, input().split())
        connection_list[con_start].append(con_end)
        connection_list[con_end].append(con_start)
    start_node, end_node = map(int, input().split())
    print("#{} {}".format(tc, BFS(connection_list, start_node, end_node)))
