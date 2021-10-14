import sys
sys.stdin = open('input.txt')

def dfs(x):
    stack = [x]
    visited[x] = 1
    while stack:
        a = stack.pop()
        print(a, end=' ')
        for i in arr_list[a]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1

def dfs1(x):
    visited[x] = 1
    print(x, end=' ')
    for i in arr_list[x]:
        if visited[i] == 0:
            dfs1(i)

arr = list(map(int, input().split()))
arr_list = [[] for i in range(8)]
visited = 8*[0]
for i in range(0, len(arr), 2):
    a = arr[i]
    b = arr[i+1]
    arr_list[a].append(b)
    arr_list[b].append(a)

dfs1(1)
# dfs(1)

