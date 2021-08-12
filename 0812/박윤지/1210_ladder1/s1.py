import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 위, 왼쪽, 오른쪽
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    k = 0

    # 도착점 i, j 구하기
    for num in range(100):
        if arr[99][num] == 2:
            i, j = 99, num

    while i > 0:
        arr[i][j] = 3
        if j == 0:
            if arr[i][j + 1] == 1:
                i += di[2]
                j += dj[2]
            else:
                i += di[0]
                j += dj[0]
        elif j == 99:
            if arr[i][j - 1] == 1:
                i += di[1]
                j += dj[1]
            else:
                i += di[0]
                j += dj[0]
        else:
            if arr[i][j+1] == 1:
                i += di[2]
                j += dj[2]
            elif arr[i][j-1] == 1:
                i += di[1]
                j += dj[1]
            elif arr[i][j+1] in [0, 3] and arr[i][j-1] in [0, 3]:
                i += di[0]
                j += dj[0]
    print('#{} {}'.format(tc, j))