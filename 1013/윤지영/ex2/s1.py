li = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
V = 7

def bfs(n):
    global load
    que = []
    visited[n] = 1
    que.append(n)
    while que:
        v = que.pop(0)
        load += str(v)
        for w in arrList[v]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = visited[n] + 1



arrList = [[] for _ in range(V+1)]
visited = [0] * (V+1)
load = ''
for i in range(len(li)//2):
    a,b = li[i*2], li[i*2+1]
    arrList[a].append(b)
    arrList[b].append(a)
bfs(1)
print('-'.join(load))