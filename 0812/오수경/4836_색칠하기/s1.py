import sys
sys.stdin = open('sample_input.txt')


# tc
# 사각형 갯수 N
# (시작점) (끝점) (색상 빨:1 파:2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]


    # 상자가 존재할 수 있는 영역
    field = []
    for f in range(10):
        field.append([0] * 10)



    # 빨간 사각형, 파란 사각형
    red = []
    blue = []
    for n in square:
        if n[-1] == 1:
            red.append(n)
        else:
            blue.append(n)



    # 빨간 사각형, 파란 사각형 한 변의 길이
    red_size = []   # 가로
    red_size2 = []  # 세로
    for rn in range(len(red)):
        width = red[rn][2] - red[rn][0]
        width2 = red[rn][3] - red[rn][1]

        red_size.append(width)
        red_size2.append(width2)


    blue_size = []
    blue_size2 = []
    for bn in range(len(blue)):
        width = blue[bn][2] - blue[bn][0]
        width2 = blue[bn][3] - blue[bn][1]

        blue_size.append(width)
        blue_size2.append(width2)




    # 빨간 사각형 크기만큼 0 -> 1
    for one in range(len(red)):
        x = red[one][0]
        x2 = red[one][1]

        for a in range(red_size[one]+1):
            for b in range(red_size2[one]+1):
                field[x + a][x2 + b] = 1


    # 파란 사각형 크기만큼 +2
    for two in range(len(blue)):
        y = blue[two][0]
        y2 = blue[two][1]


        for m in range(blue_size[two]+1):
            for n in range(blue_size2[two]+1):
                field[y + m][y2 + n] += 2

    # print(field)
    cnt = 0
    for i in range(10):
        for j in range(10):
            if field[i][j] >= 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

