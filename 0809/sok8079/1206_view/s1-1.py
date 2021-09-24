import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())    #테스트 케이스 길이
    building_h = list(map(int, input().split())) #빌딩의 높이들
    result = 0 #조망권 확보수

    for i in range(2, L-2):
        height = building_h[i]
        temp_top = 0
        for j in range(4):
            idx = [-2, -1, 1, 2]
            if building_h[i+idx[j]] > temp_top:
                temp_top = building_h[i+idx[j]]

    if height > temp_top:
        result += height - temp_top
    print('#{} {}'.format(tc, result))