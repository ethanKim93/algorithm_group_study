sample = "1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7"
sample = list(map(int, sample.split(',')))

edges = [[] for _ in range(10)]

for i in range(len(sample)//2):
    edges[sample[i*2]].append(sample[i*2+1])
    edges[sample[i*2+1]].append(sample[i*2])

visited = [0] * 10
queue = [1]
visited[1] = 1
result = "1"

while queue:
    v = queue.pop(0)
    for node in edges[v]:
        if not visited[node]:
            visited[node] = 1
            result += '-' + str(node)
            queue.append(node)

print(result)