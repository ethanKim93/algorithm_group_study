import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    building_view = 0
    for i in range(2, L - 2):
        view_left2 = buildings[i] - buildings[i - 2]
        view_left1 = buildings[i] - buildings[i - 1]
        view_right1 = buildings[i] - buildings[i + 1]
        view_right2 = buildings[i] - buildings[i + 2]
        if view_left2 > 0 and view_left1 > 0 and view_right1 > 0 and view_right2 > 0:
            min_view = view_left2
            for view in [view_left2, view_left1, view_right1, view_right2]:
                if min_view > view:
                    min_view = view
            building_view += min_view

    print("#{} {}".format(tc, building_view))



