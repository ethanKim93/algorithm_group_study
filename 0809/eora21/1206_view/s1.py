import sys
sys.stdin = open('input.txt')
for case in range(10):
    L = int(input()) # 빌딩갯수
    buildings = list(map(int, input().split())) # 빌딩생성, 좌우 2칸씩 맨땅

    total = 0
    for i in range(2, L - 2): # 좌우 2칸씩 뺌
        i_adder = 0 # for문 빨리 돌리기 위해

        LR = []

        LR.append(buildings[i] - buildings[i - 1]) #왼쪽 2개 빌딩 차이
        LR.append(buildings[i] - buildings[i - 2])

        LR.append(buildings[i] - buildings[i + 1]) #오른쪽 2개 빌딩 차이
        LR.append(buildings[i] - buildings[i + 2])

        if LR[2] > 0:
            i_adder = 1
            if LR[3] > 0:
                i_adder = 2
                for A in range(3):
                    for B in range(3 - A):
                        if LR[B] > LR[B + 1]:
                            LR[B], LR[B + 1] = LR[B + 1], LR[B]
                if LR[0] > 0:
                    total += LR[0]

        i += i_adder

    print("#{} {}".format(case + 1, total))