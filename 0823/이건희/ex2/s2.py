def DFS(idx):
    global total, ans

    if total == 10: # Sum 10 -> return
        subans = []
        for i in range(len(powerset)):
            if temps[i]:
                subans.append(powerset[i-1])
        ans.append(subans)
        return

    if idx == len(powerset): # Max idx -> return
        return

    # Make subset
    temps[idx] = 1
    total += powerset[idx-1]
    DFS(idx+1)
    temps[idx] = 0
    total -= powerset[idx-1]
    DFS(idx+1)

powerset = [1,2,3,4,5,6,7,8,9,10]
temps = [0]*10
ans = [] # Subset list
total = 0

DFS(0)

print(ans)