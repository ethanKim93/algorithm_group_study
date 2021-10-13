A = [[1, 2],[1, 3],[2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
tree = [[] for _ in range(8)]
for i in A:
    tree[i[0]].append(i[1])
    tree[i[1]].append(i[0])
print(tree)
visited = []
stack = [1]

def dfs():

    while stack:
        V = stack.pop(-1)
        if V not in visited:
            visited.append(V)

            for j in tree[V]:
                if j not in visited:
                    stack.append(j)
dfs()
print(visited)