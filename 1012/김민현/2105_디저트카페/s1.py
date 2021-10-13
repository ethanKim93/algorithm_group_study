#미구현
import sys
sys.stdin = open('sample_input.txt')

#dir = [0,1,2,3]
ds = [(-1,1),(-1,-1),(1,-1),(1,1)]


def solution(x,y,dir):
    global cnt
    global maxcnt

    if dir == 4:
        print(cnt)
        if maxcnt < cnt:
            maxcnt = cnt
        visit = []
        return

    dx = x + ds[dir][0]
    dy = y + ds[dir][1]
    #print(dx,dy)
    if 0<= dx <N and 0<=dy<N:
            cnt += 1
            visit.append()
            solution(dx,dy,dir)
    else:
        dir += 1
        solution(x,y,dir)




T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    maxcnt = N*N

    for i in range(N):
        for j in range(N):
            cnt = 0
            visit = []
            solution(i,j,0)

    if mincnt == N*N:
        mincnt = -1
    print('#{} {}'.format(tc,mincnt))