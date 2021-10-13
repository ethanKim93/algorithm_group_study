sample = "1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7"
sample = list(map(int, sample.split(',')))

def dfs(result, v):
    if len(result) == 13:
        print(result)
        return

    visited[v] = 1
    for w in edges[v]:
        if not visited[w]:
            dfs(result+'-'+str(w), w)
    visited[v] = 0

edges = [[] for _ in range(10)]

for i in range(len(sample)//2):
    edges[sample[i*2]].append(sample[i*2+1])
    edges[sample[i*2+1]].append(sample[i*2])

visited = [0] * 10

dfs('1', 1)



