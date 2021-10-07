# 1 2 3 4 5 6 7 8 9 10
A = list(map(int, input().split()))

visited = [0] * len(A)
lim = 10

def backtrack(s, tot):
    global visited, lim, A
    if s > len(A):
        return
    if tot >= lim:
        if tot == lim:
            for ind in range(len(A)):
                if visited[ind]:
                    print(A[ind], end=' ')
            print()
        return

    for i in range(s, len(A)):
        if not visited[i]:
            visited[i] = 1
            backtrack(i+1, tot+A[i])
            visited[i] = 0

backtrack(0, 0)