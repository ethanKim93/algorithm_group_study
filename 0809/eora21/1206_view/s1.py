import sys
sys.stdin = open("input.txt")

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

        if LR[2] > 0: # 오른쪽 첫번째 빌딩보다 높다면
            i_adder = 1 # 오른쪽 첫번째 빌딩은 어차피 크기가 작으니 볼 필요 없다.
            if LR[3] > 0: # 두번째 빌딩도 마찬가지
                i_adder = 2
                for A in range(3): # 두번째 빌딩까지 높다면 좌우 2개 층 차이 버블정렬
                    for B in range(3 - A):
                        if LR[B] > LR[B + 1]:
                            LR[B], LR[B + 1] = LR[B + 1], LR[B]
                if LR[0] > 0: # 최솟값이 양수로 해당 빌딩이 조망권 확보가 됐다면
                    total += LR[0] # 추가

        i += i_adder

    print("#{} {}".format(case + 1, total))