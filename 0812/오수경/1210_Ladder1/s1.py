import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    t = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]


    # 상 좌 우
    di = [-1, 0, 0]
    dj = [0, -1, 1]


    k = 0
    # 시작 위치 찾기(아래 -> 위)
    i, j = 99, 0
    for a in range(102):
        if ladder[99][a] == 2:
            j = a


    # i == 0 도달할때까지 위로 이동
    while i != 0:
        k = 0   # 위로 이동
        ni = i + di[k]
        nj = j + dj[k]

        i, j = ni, nj

        if ladder[ni][nj-1] == 1:
            while ladder[ni][nj-1] == 1:
                k = 1  # 왼쪽
                ni = i + di[k]
                nj = j + dj[k]
                i, j = ni, nj

        elif ladder[ni][nj+1] == 1:
            while ladder[ni][nj+1] == 1:
                k = 2  # 오른쪽
                ni = i + di[k]
                nj = j + dj[k]
                i, j = ni, nj



    print("#{} {}".format(tc, j-1))