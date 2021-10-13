A = [[1, 2],[1, 3],[2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
tree = [[] for _ in range(8)]
for i in A:
    tree[i[0]].append(i[1])
    tree[i[1]].append(i[0])

visited = []
queue = [1]

def bfs():

    while queue:
        V = queue.pop(0)
        if V not in visited:
            visited.append(V)

            for j in tree[V]:
                if j not in visited:
                    queue.append(j)
bfs()
print(visited)