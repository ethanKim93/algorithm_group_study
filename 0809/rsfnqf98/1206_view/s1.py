import sys

sys.stdin = open('input.txt')

for tc in range(1, 11) :
    L = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, len(buildings) - 2) :
        temp_heights = [buildings[i-2], buildings[i-1],buildings[i+1], buildings[i+2]] 
        # 좌우로 2개 집에 대한 임시적인 리스트 형성
        temp_max = temp_heights[0]
        for temp_height in temp_heights :
            if temp_max < temp_height :
                temp_max = temp_height
        # 해당 임시 리스트의 최대 값 temp_max에 저장
        if temp_max < buildings[i] :
            result += buildings[i] - temp_max
        # temp_max보다 buildings[i]가 크면, 조망권을 확보하는 집을 result에 더한다.
    print("#{} {}".format(tc, result))