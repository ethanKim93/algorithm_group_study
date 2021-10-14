def bfs(adj):
    front = -1
    rear = 0
    queue = [0] * len(adj)
    queue[rear] = 1
    visited[1] = 1
    while front < rear:
        front += 1
        check = queue[front]
        print(check)
        for new_check in adj[check]:
            if not visited[new_check]:
                visited[new_check] = 1
                rear += 1
                queue[rear] = new_check
    return
    
def to_adj():
    adj = [[] for _ in range(len(input_data))]
    idx = 0
    while idx < len(input_data):
        adj[input_data[idx]].append(input_data[idx + 1])
        adj[input_data[idx + 1]].append(input_data[idx])
        idx += 2
    return adj


input_data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * 8

bfs(to_adj())