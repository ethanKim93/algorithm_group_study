def bfs(start):
    q = [start]
    while q:
        n = q.pop(0)
        if not visited[n]:
            visited[n] = 1
            if n == start:
                print(str(n),end="")
            else:
                print("-" + str(n) , end="")
            for i in tree_maps[n]:
                if not visited[i]:
                    q.append(i)

ex_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

tree_maps = [[] for _ in range(len(ex_list)+1)]
visited = [0]*(len(ex_list)+1)

for i in range(0,len(ex_list),2):
    tree_maps[ex_list[i]].append(ex_list[i+1])
    tree_maps[ex_list[i+1]].append(ex_list[i])

bfs(1)