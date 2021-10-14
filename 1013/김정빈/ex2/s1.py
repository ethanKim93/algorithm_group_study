al = "1213242546566737"
adjlist = [[] for _ in range(8)]
for i in range(0, len(al), 2):
    adjlist[int(al[i])].append(int(al[i+1]))
    adjlist[int(al[i+1])].append(int(al[i]))
visited = [0]*10
print(adjlist)

queue = [1]
def bfs():
    while queue:
        temp = queue.pop(0)
        if not visited[temp]:
            visited[temp] = 1
            print(temp, end=" ")
        for node in adjlist[temp]:
            if not visited[node]:
                queue.append(node)
    return
bfs()
