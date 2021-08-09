import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    length = int(input())
    buildings = list(map(int,input().split()))

    i = 0
    view = 0
    while(i < length-4):# index from 0(0~5) to length-5(length-5 ~ length)
        #5개 중 max의 크기와 index 찾기
        ind = max1 = 0
        for idx, building in enumerate(buildings[i:i+5]):
            if max1 < building:
                max1 = building
                ind = idx
        #가운데를 제외한 나머지 리스트의 최대값
        max2 = 0
        if ind == 2:
            for building in buildings[i:i+2]+buildings[i+3:i+5]:
                if max2 < building:
                    max2 = building
            i += 3 #가운데가 제일 큰 경우 다음 2번째까지는 최대가 될 수 없으므로 +3
            view += max1-max2
        else:
            i += 1

    print('#{} {}'.format(tc,view))