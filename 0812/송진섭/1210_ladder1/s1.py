import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [-1, 0, 0]  # 위 오른쪽 왼쪽 이동
    dj = [0, 1, -1]
    col = 0
    row = 99
    direction = 0  # 방문여부를 위해 방향표시 0: 이전에 위로이동 1: 오른쪽이동 2: 왼쪽이동

    for j in range(100):  # 도착점 x 찾기
        if ladder[99][j] == 2:
            col = j
            break

    while row:  # 도착점에서 시작점찾으러 출발
        if (direction == 0 or direction == 1) and col != 99 and ladder[row][col+1]:  # 오른쪽으로 갈 수 있는지 여부확인
            col += dj[1]
            direction = 1
        elif (direction == 0 or direction == 2) and col != 0 and ladder[row][col-1]:  # 왼쪽으로 갈 수 있는지 여부확인
            col += dj[2]
            direction = 2
        else:
            row += di[0]  # 위로 이동
            direction = 0
        if row == 0:
            print('#{} {}'.format(tc, col))