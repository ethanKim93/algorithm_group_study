import sys
sys.stdin = open('input.txt')


def move(r, c):
    dj = [1, -1, 0]
    k = 2
    r -= 1
    while r:
        # 오른쪽
        if dj[k] == 1:
            # 위로 갈 수 있는 지 확인
            if li[r - 1][c] == 1:
                r -= 1
                k = 2
            else:
                c += 1

        # 왼쪽
        elif dj[k] == -1:
            # 위로 갈 수 있는 지 확인
            if li[r - 1][c] == 1:
                r -= 1
                k = 2
            else:
                c -= 1
        else:
            # 오른쪽 갈 수 있는지 확인
            if 0 <= c + 1 < 100 and li[r][c + 1] == 1:
                c += 1
                k = 0
            # 왼쪽으로 갈 수 있는지 확인
            elif 0 <= c - 1 < 100 and li[r][c - 1] == 1:
                c -= 1
                k = 1
            else:
                r -= 1
    return c


for _ in range(10):
    tc = int(input())
    li = []
    for _ in range(100):
        li += [list(map(int,input().split()))]

    end_i = end_j = 99
    for i in range(100):
        for j in range(100):
            if li[i][j] == 2:
                end_i = i
                end_j = j

    nj = move(end_i, end_j)
    print('#{} {}'.format(tc, nj))




