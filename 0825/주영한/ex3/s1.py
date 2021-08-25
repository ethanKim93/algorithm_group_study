import sys
sys.stdin = open("input.txt")

# 인접 행렬과 리스트로 구현된 큐
def BFS(matrix, start):
    start -= 1
    visited = [0] * (len(matrix))
    queue = [start]
    visited[start] = 1
    while queue:
        node = queue.pop(0)
        print(node + 1, end=" ")
        for i in range(len(matrix)):
            if matrix[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1
    print()
    print("depth of the nodes : {}".format(visited))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    connections = list(map(lambda x : int(x) - 1, input().split()))

    for idx in range(M):
        matrix[connections[2 * idx]][connections[2 * idx + 1]] = 1

    BFS(matrix, 1)