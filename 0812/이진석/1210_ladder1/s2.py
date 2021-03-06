import sys

sys.stdin = open('input.txt')


def check_xy(arr, x, y, sideflag):
    di = [-1, 0, 0]  # 상 좌 우
    dj = [0, -1, 1]
    list_k = [0, 2, 1, 0]       # sideflag가 0일때 좌측&우측&상단탐색, 1일때 좌측&상단탐색, 2일때 우측&상단 탐색
    list_k.remove(list_k[sideflag])
    for k in list_k:
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni <= 99 and 0 <= nj <= 99 and arr[ni][nj]:
            y = nj
            x = ni
            sideflag = k
            break
    return x, y, sideflag


for tc in range(1, 11):
    N = int(input())
    ladder = []
    flag = 0  # 0일때 위쪽(탐색) 1일때 좌측 2일때 우측으로 신호를 주기위한 변수
    now_i = 0
    now_j = 0

    for _ in range(100):  # 입력받기
        ladder.append(list(map(int, input().split())))
    for j in range(100):  # 초기 j값 찾기 (문제에서는 x값)
        if ladder[99][j] == 2:
            now_i = 99
            now_j = j
            break
    i = 99  # 초기값
    j = now_j
    while i > 0:
        i, j, flag = check_xy(ladder, i, j, flag)
        answer = j
    print('#{} {}'.format(N, answer))
