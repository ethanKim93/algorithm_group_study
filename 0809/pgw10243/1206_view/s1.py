import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    length = int(input())
    buildings = list(map(int,input().split()))

    i = 0
    view = 0
    while(i < length-4):
        ind = max1 = 0
        for idx, building in enumerate(buildings[i:i+5]):
            if max1 < building:
                max1 = building
                ind = idx

        max2 = 0
        if ind == 2:
            for building in buildings[i:i+2]+buildings[i+3:i+5]:
                if max2 < building:
                    max2 = building
            i += 3
            view += max1-max2
        else:
            i += 1

    print('#{} {}'.format(tc,view))