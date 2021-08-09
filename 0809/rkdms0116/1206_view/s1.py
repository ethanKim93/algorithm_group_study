import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    L = int(input())
    buildings = list(map(int, input().split()))
    view_point_cnt = 0
    for num in range(2,L-2):
        around_max_building = buildings[num-2]
        if around_max_building < buildings[num-1]:
            around_max_building = buildings[num-1]
        if around_max_building < buildings[num+1]:
            around_max_building = buildings[num+1]
        if around_max_building < buildings[num+2]:
            around_max_building = buildings[num+2]
        if buildings[num] > around_max_building:
            view_point_cnt += buildings[num] - around_max_building
    print('#{} {}'.format(tc, view_point_cnt))