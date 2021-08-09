import sys
sys.stdin = open('input.txt')
region = []
answer = []
for test in range(10):
    ground = int(input())
    buildings = list(map(int, input().split()))
    region.append(buildings)

for i_buildings in region:
    good_view_home = 0
    for i in range(2, len(i_buildings)-2):
        higher_building = i_buildings[i]-i_buildings[i-2]
        case=[i_buildings[i-2],i_buildings[i-1],i_buildings[i+1],i_buildings[i+2]]
        for side in case:
            if i_buildings[i]-side < higher_building:
                higher_building = i_buildings[i]-side

        if higher_building > 0:
            good_view_home += higher_building
    answer.append(good_view_home)
for idx,i in enumerate(answer):
    print('#{0} {1}'.format(idx+1,i))