import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [-1, 0, 0]  # 위 오른쪽 왼쪽 이동
    dj = [0, 1, -1]
    col = 0
    row = 99

    for j in range(100):  # 도착점 x 찾기
        if ladder[99][j] == 2:
            col = j
            break

    while row:  # 도착점에서 시작점찾으러 출발
        if col != 99 and ladder[row][col+1]:  # 오른쪽으로 갈 수 있는지 여부확인
            ladder[row][col] = 0  # 방문이력
            col += dj[1]
        elif col != 0 and ladder[row][col-1]:  # 왼쪽으로 갈 수 있는지 여부확인
            ladder[row][col] = 0  # 방문이력
            col += dj[2]
        else:
            row += di[0]  # 위로 이동
        if row == 0:
            print('#{} {}'.format(tc, col))