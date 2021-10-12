# 해결을 못하였습니다..
import sys
sys.stdin = open('sample_input.txt')

# 시계방향 대각선
dy = [1,1,-1,-1]
dx = [1,-1,-1,1]

def cafe_tour(x,y,k,cnt):
    global sx, sy, max_cnt

    if k == 3 and x == sx and y == sy:
        if max_cnt < cnt:
            max_cnt = cnt
    elif x < 0 or x >= N or y < 0 or y >= N:
        return
    elif dessert_cafe[y][x] in start_point:
        return

    else:
        start_point.append(dessert_cafe[y][x])

        if k == 0 or k==1:
            cafe_tour(x+dx[k],y+dy[k],k,cnt+1)
            cafe_tour(x+dx[k+1],y+dy[k+1],k+1,cnt+1)
        elif k == 2:
            if x+y != sx+sy:
                cafe_tour(x+dx[2], y+dy[2], k, cnt+1)
            else:
                cafe_tour(x+dx[3], y+dy[3], k+1, cnt+1)
        else:
            cafe_tour(x+dx[3], y+dy[3],k,cnt+1)

        start_point.remove(dessert_cafe[y][x])



T = int(input())
for tc in range(1, T+1):

    N = int(input())
    dessert_cafe = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    start_point =[]
    for i in range(N):
        for j in range(N):
            sy = i
            sx = j
            start_point.append(dessert_cafe[i][j])
            cafe_tour(i+1,j+1,0,1)
            start_point.remove(dessert_cafe[i][j])

    print('#{} {}'.format(tc,max_cnt))