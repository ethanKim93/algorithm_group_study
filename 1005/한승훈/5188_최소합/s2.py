import sys
sys.stdin = open('sample_input.txt')


def dfs(start, tot):
    global mn
    if tot > mn: # 시간초과땜에 중간에 넘어가면 그만둠
        return
    if start == (n-1, n-1): # 끝까지 오면 끝내기
        if tot <= mn:
            mn = tot
        return

    for k in range(2):
        ni, nj = start[0] + dir[k][0], start[1] + dir[k][1]
        if 0 <= ni < n and 0 <= nj < n:
            dfs((ni,nj), tot+arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mn = 9999 # 최소 값
    dir = [(0,1), (1,0)] # 우 하

    dfs((0,0), arr[0][0])
    print('#{} {}'.format(tc, mn))