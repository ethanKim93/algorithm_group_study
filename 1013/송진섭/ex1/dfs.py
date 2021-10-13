"""
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(v):
    stack.append(v)
    visited[v] = 1
    while stack:
        s = stack.pop()
        print(s)
        for w in adj_list[s]:
            if not visited[w]:
                visited[w] = 1
                stack.append(w)

def recursice_dfs(v):
    visited[v] = 1
    print(v)
    for w in adj_list[v]:
        if not visited[w]:
            recursice_dfs(w)

N = 7
stack = []
visited = [0 for _ in range(N+2)]
edge = list(map(int, input().split()))
adj_list = [[] for _ in range(N+1)]
for i in range(0, len(edge), 2):
    adj_list[edge[i]].append(edge[i+1])
    adj_list[edge[i+1]].append(edge[i])
recursice_dfs(1)


