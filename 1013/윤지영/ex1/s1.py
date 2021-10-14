
def dfs(n):
    global load
    visited[n] = 1
    load += str(n)
    if len(load) == V:
        return
    for w in arrList[n]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)


li = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
V = 7
visited =[0] * (V+1)
arrList = [[] for _ in range(V+1)]
for i in range(len(li)//2):
    a,b = li[i*2], li[i*2+1]
    arrList[a].append(b)
    arrList[b].append(a)
load = ''
dfs(1)
print('-'.join(load))