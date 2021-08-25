import sys
sys.stdin = open("input.txt")

# 인접 리스트와 리스트로 구현된 큐
def BFS(matrix, start, N):
    start -= 1
    visited = [0] * N
    queue = [start]
    visited[start] = 1
    while queue:
        node = queue.pop(0)
        print(node + 1, end=" ")
        for i in matrix[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1
    print()
    print("depth of the nodes : {}".format(visited))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    connected_list = [[] for _ in range(N)]
    connections = list(map(lambda x : int(x) - 1, input().split()))

    for idx in range(M):
        connected_list[connections[2 * idx]].append(connections[2 * idx + 1])

    BFS(connected_list, 1, N)