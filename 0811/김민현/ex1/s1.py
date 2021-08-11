import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for tc in range(1,T+1):
    result = 0
    N = int(input())
    ary = []
    for i in range(N):
       row = list(map(int,input().split()))
       ary.append(row)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                x,y = i,j
                if i+dx[k] >= 0 and i+dx[k] < N:
                    x = i + dx[k]
                if j+dy[k] >= 0 and j+dy[k] < N:
                    y = j + dy[k]
                temp = ary[i][j] - ary[x][y]
                if temp < 0:
                    temp = temp*-1
                result += temp
    print(result)