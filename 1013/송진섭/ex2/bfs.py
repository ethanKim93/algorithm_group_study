"""
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


def bfs(v):
    queue = [v]
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    while queue:
        front = queue[0]
        del queue[0]
        print(front)
        for j in range(1, N+1):
            if adj_matrix[front][j] and not visited[j]:
                queue.append(j)
                visited[j] = 1


N = 7

edge = list(map(int, input().split()))
adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(0, len(edge), 2):
    adj_matrix[edge[i]][edge[i+1]] = 1
    adj_matrix[edge[i + 1]][edge[i]] = 1
# print(adj_matrix)
bfs(1)