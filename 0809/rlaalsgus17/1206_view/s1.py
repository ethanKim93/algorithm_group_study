import sys
sys.stdin =open('input.txt')

for tc in range(1,11):
    L = int(input())
    buildings = list(map(int,input().split()))
    #print(L)
    #print(buildings)

    result = 0
    for b_idx in range(2,len(buildings)-2):
        '''
        pre_buiding1 =  buildings[b_idx] - buildings[b_idx-1]
        pre_buiding2 =  buildings[b_idx] - buildings[b_idx-2]
        next_buiding1 = buildings[b_idx] - buildings[b_idx + 1]
        next_buiding2 = buildings[b_idx] - buildings[b_idx + 2]
        '''
        #양옆 2개의 층수 차이 확인
        dif_floor = []
        for i in range(-2,3):
            dif_floor.append(buildings[b_idx] - buildings[b_idx+i])

        #가장 낮은 층수와 높은 층수 확인
        min_floor = dif_floor[0]
        for j in dif_floor:
            if min_floor > j and j != 0:
                min_floor = j

        if min_floor > 0:
            result += min_floor
    print(result)


