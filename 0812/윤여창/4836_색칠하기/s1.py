import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    white_map =[[0]*10 for i in range(10)]
    cunt = 0

    for i in range(N):
        r1,c1,r2,c2,color = map(int, input().split())
        for k in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1:
                    if white_map[k][j] == 0:         #내가 칠해야 할 색깔이 빨강인데 하얀맵 위치가 백지면 빨강칠하기
                        white_map[k][j] = 1          # 만약 파란색이 먼저 칠해져있다면 겹치게 되니까 cunt +1
                    elif white_map[k][j] == 2:
                        cunt += 1
                else:
                    if white_map[k][j] == 0:
                        white_map[k][j] = 2
                    elif white_map[k][j] == 1:
                        cunt += 1

    print('#{} {}'.format(tc, cunt))