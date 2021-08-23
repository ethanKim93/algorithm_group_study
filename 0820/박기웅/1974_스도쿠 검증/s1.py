import sys
sys.stdin = open("input.txt")

def check(arr):
    for i in range(9):
        cnt1 = [0]*10               # 가로 검사용 카운트 리스트
        cnt2 = [0]*10               # 세로 검사용 카운트 리스트
        for j in range(9):
            cnt1[arr[i][j]] += 1
            if cnt1[arr[i][j]] > 1:
                return 0
            cnt2[arr[j][i]] += 1
            if cnt2[arr[j][i]] > 1:
                return 0

    for k in range(0, 9 ,3):
        for l in range(0, 9 ,3):
            cnt3 = [0]*10           # 3x3 box 검사용 카운트 리스트
            for i in range(k, k+3):
                for j in range(l, l+3):
                    cnt3[arr[i][j]] += 1
                    if cnt3[arr[i][j]] > 1:
                        return 0
    return 1



for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, check(arr)))

    