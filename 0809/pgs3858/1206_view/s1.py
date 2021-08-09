import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    total = 0

    for i in range(2, len(buildings)-2):
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            max_height = buildings[i-2]
            for k in range(i-1, i+3):
                if buildings[i] == buildings[k]:
                    continue;
                elif max_height < buildings[k]:
                    max_height = buildings[k]
            total += (buildings[i] - max_height)

    print('#{} {}'.format(tc, total))
