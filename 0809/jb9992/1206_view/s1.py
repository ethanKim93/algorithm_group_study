import sys
sys.stdin = open('input.txt')

BiggestOne = 0

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    total = 0

    for i in range(0, L):
        if buildings[i] == 0:
            continue
        elif buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2] and buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
            if buildings[i-2] >= buildings[i-1] and buildings[i-2] >= buildings[i+1] and buildings[i-2] >= buildings[i+2]:
                BiggestOne = buildings[i-2]
            elif buildings[i-1] >= buildings[i-2] and buildings[i-1] >= buildings[i+1] and buildings[i-1] >= buildings[i+2]:
                BiggestOne = buildings[i-1]
            elif buildings[i+1] >= buildings[i-1] and buildings[i+1] >= buildings[i-1] and buildings[i+1] >= buildings[i+2]:
                BiggestOne = buildings[i+1]
            else:
                BiggestOne = buildings[i+2]
            total += (buildings[i] - BiggestOne)
    print('#{} {}'.format(tc, total))


