al = "1213242546566737"
adjlist = [[] for _ in range(8)]
for i in range(0, len(al), 2):
    adjlist[int(al[i])].append(int(al[i+1]))
    adjlist[int(al[i+1])].append(int(al[i]))
visited = [0]*10
stack = []
print(adjlist)
def dfs():
    stack.append(1)
    while stack:
        temp = stack.pop()
        if visited[temp] == 0:
            visited[temp] = 1
            print(temp, end=" ")
            for node in adjlist[temp]:
                stack.append(node)
    return
dfs()
