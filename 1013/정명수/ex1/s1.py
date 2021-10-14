li = list(map(int,input().split()))
adj_list = [[] for _ in range(10)]
visited = [0]*10
for i in range(0,len(li),2):
    adj_list[li[i]].append(li[i+1])
    adj_list[li[i+1]].append(li[i])
def dfs(n):
    print(n,end = " ")
    visited[n] = 1
    for i in adj_list[n]:
        if not visited[i]:
            dfs(i)
dfs(1)