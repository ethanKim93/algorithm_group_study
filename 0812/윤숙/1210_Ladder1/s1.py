import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N=int(input())
    LadderMap = [list(map(int, input().split())) for _ in range(100)]

    terminusRow = 0
    terminusCol = 0
    for j in range(100):
        for i in range(100):
            if LadderMap[i][j] == 2:
                terminusRow = i
                terminusCol = j
                break

    T_R = terminusRow  ##99
    T_C = terminusCol  ##57
    # 상 좌 우
    DR = [-1, 0, 0]
    DC = [0, -1, 1]
    F = 0
    while True:

        if T_R == 0:
            break

        T_R = T_R + DR[F]
        T_C = T_C + DC[F]
        #
        if LadderMap[T_R][T_C] == 1 and LadderMap[T_R][T_C - 1] == 1 :  # 왼쪽에 1 일때 1 #직진할지 오른쪽갈지 판단
            F = 1
        #직진 010
        elif LadderMap[T_R][T_C] == 1 and LadderMap[T_R][T_C - 1] == 0 and LadderMap[T_R][T_C + 1] == 0 :   # 왼쪽에 0 일때 1
            F = 0

        elif LadderMap[T_R][T_C] == 1 and LadderMap[T_R][T_C+1] == 1:  # 오른쪽에 1 일때 1
            F = 2

        elif LadderMap[T_R][T_C] == 1 and LadderMap[T_R][T_C + 1] == 0:  # 오른쪽에 0 일때 1 #직진할지 왼쪽으로 갈지 판단.
            F = 2

        elif LadderMap[T_R][T_C - 1] == 0 and LadderMap[T_R][T_C] == 2:
            F = 0

    print(T_C)
