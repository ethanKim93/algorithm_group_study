import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    t = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]



    k = 0
    # 시작 위치 찾기(아래 -> 위)
    i, j = 99, 0
    for a in range(102):
        if ladder[99][a] == 2:
            j = a


    # i == 0 도달할때까지 위로 이동
    while i != 0:
        i -= 1

        if ladder[i][j-1] == 1:
            while ladder[i][j-1] == 1:
                j -=1

        elif ladder[i][j+1] == 1:
            while ladder[i][j+1] == 1:
                j += 1


    print("#{} {}".format(tc, j-1))