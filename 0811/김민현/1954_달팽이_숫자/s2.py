import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())


for tc in range(1,T+1):
    N = int(input())

    result = [[0]*N for k in range(N)]

    x,y = -1,0
    dir = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            cnt += 1
            if i != N-1:
               x = i + dx[dir]               y = j + dy[dir]
               result[x][y] = cnt
    #출력
    for i in range(N):
        print(result[i])

