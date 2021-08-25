n = 7
maps = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
temps = [[0] * (n + 1) for _ in range(n + 1)]

for i, x in maps:
    temps[i][x] = 1
    temps[x][i] = 1

s = 1
visited = [0]*(n+1)
q = []
q.append(1)

# 1
while q:
    pos = q.pop(0)
    if not visited[pos]:
        visited[pos] = 1
        print("-" + str(pos), end="")
        for i in range(n+1):
            if temps[pos][i] == 1:
                q.append(i)

# 2
while q:
    pos = q.pop(0)
    if not visited[pos]:
        visited[pos] = 1
        print("-" + str(pos), end="")
        for i in range(n+1):
            if temps[pos][i] == 1 and not visited[i]: # 이미 경로 지난 건 안 넣어서 while 덜 돌 수 있음
                q.append(i)

# 3
visited[s] = 1
while q:
    pos = q.pop(0)
    print(pos)
    for i in range(n+1):
        if temps[pos][i] == 1 and not visited[i]:
            q.append(i)
            visited[i] = visited[pos]+1 # visited에 최단경로 기록