import sys
sys.stdin = open('input.txt')
def search(w,len,flag):
    global max_len
    visited[w[0]][w[1]] = 1
    if len > max_len:
        max_len = len
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        if 0 <= dx[i]+w[0] < N and 0 <= dy[i]+w[1] < N and not visited[dx[i]+w[0]][dy[i]+w[1]]:
            if arr[dx[i]+w[0]][dy[i]+w[1]] < arr[w[0]][w[1]]:
                search((dx[i]+w[0], dy[i]+w[1]), len+1,flag)
            elif flag and arr[dx[i]+w[0]][dy[i]+w[1]]-K < arr[w[0]][w[1]]:
                tmp = arr[dx[i]+w[0]][dy[i]+w[1]]
                arr[dx[i]+w[0]][dy[i]+w[1]] = arr[w[0]][w[1]]-1
                search((dx[i]+w[0], dy[i]+w[1]), len+1, 0)
                arr[dx[i]+w[0]][dy[i]+w[1]] = tmp
    visited[w[0]][w[1]] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    hightop = arr[0][0]
    hightops = []
    max_len = 0
    flag = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= hightop:
                hightop = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == hightop:
                hightops.append((i,j))
    for top in hightops:
        search(top,1,flag)
    print('#{} {}'.format(tc,max_len))