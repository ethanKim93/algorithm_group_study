import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail_list = [[0]*N for _ in range(N)]

    #이동 방향을 나타내는 drdc와 direction을 정의한다.
    drdc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0

    #현재 위치를 정의하는 row, col을 정의한다.
    row = 0
    col = 0

    for number in range(1, N*N + 1):
        # 해당 위치에 번호를 매긴다.
        snail_list[row][col] = number

        # 다음 위치를 확인해본다.
        temp_row = row + drdc[direction % 4][0]
        temp_col = col + drdc[direction % 4][1]

        # 다음 위치에 숫자가 있거나, 범위 밖으로 나가게되면 방향을 바꾸어준다.
        if temp_row < 0 or temp_row > N-1 or temp_col < 0 or temp_col > N-1 or snail_list[temp_row][temp_col]:
            direction += 1

        # 바꿔준 방향으로(또는 기존 방향으로) 이동한 위치로 업데이트 한다.
        row += drdc[direction % 4][0]
        col += drdc[direction % 4][1]

    print("#{}".format(tc))
    for i in range(N):
        print(" ".join(map(str, snail_list[i])))
