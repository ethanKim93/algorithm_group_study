def dfs(adj):
    stack = [1]
    while stack:
        check = stack.pop()
        if visited[check] == 1:
            continue
        visited[check] = 1
        print(check)
        for new_check in adj[check]:
            if not visited[new_check]:
                stack.append(new_check)
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

dfs(to_adj())