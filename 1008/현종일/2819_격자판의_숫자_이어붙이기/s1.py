import sys
sys.stdin = open("sample_input.txt")

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def find_seven(now_x, now_y, seven):
    if len(seven) == 7:
        if seven not in result_arr:
            result_arr.append(seven)
        return

    for arrow in range(4):
        nx = now_x + dx[arrow]
        ny = now_y + dy[arrow]
        if 0 <= nx <= 3 and 0 <= ny <= 3:
            find_seven(nx, ny, seven+str(field[nx][ny]))

for tc in range(1, int(input())+1):
    field = [list(map(int, input().split())) for _ in range(4)]
    result_arr = []
    for i in range(4):
        for j in range(4):
            find_seven(i, j, str(field[i][j]))

    print('#{} {}'.format(tc, len(result_arr)))
