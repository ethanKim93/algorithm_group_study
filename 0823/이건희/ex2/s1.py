def DFS(idx):
    global ans, temps, pre_ans

    if idx == len(maps):
        pre_ans = []
        for i in range(len(maps)):
            if temps[i]:
                pre_ans.append(maps[i])
        ans.append(pre_ans)
        return

    temps[idx] = 1
    DFS(idx+1)
    temps[idx] = 0
    DFS(idx+1)


maps = [1, 2, 3]
temps = [0]*3
ans = []
DFS(0)
print(ans)