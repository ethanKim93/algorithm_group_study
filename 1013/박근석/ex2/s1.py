import sys
sys.stdin = open('input.txt')

def bfs(x):
    queue = [x]
    visited[x] = 1
    while queue:
        a = queue.pop(0)
        print(a, end=' ')
        for i in arr_list[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

arr = list(map(int, input().split()))
arr_list = [[] for i in range(8)]
visited = 8*[0]
for i in range(0, len(arr), 2):
    a = arr[i]
    b = arr[i+1]
    arr_list[a].append(b)
    arr_list[b].append(a)

bfs(1)
