import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    li = []
    for k in range(N):
        li += [list(map(int,input().split()))]
    di = [0,0,-1,1]
    dj = [-1,1,0,0]
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N :
                    li_abs = abs(li[i][j] - li[ni][nj])
                    result += li_abs
    print('#{} {}'.format(tc,result))



