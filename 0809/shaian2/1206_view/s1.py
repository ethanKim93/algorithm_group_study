import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, L-2):
        left = 0
        right = 0
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
            if buildings[i-1] > buildings[i-2]:
                left = buildings[i] - buildings[i-1]
            else:
                left = buildings[i] - buildings[i-2]
        if buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            if buildings[i+1] > buildings[i+2]:
                right = buildings[i] - buildings[i+1]
            else:
                right = buildings[i] - buildings[i+2]
        if left != 0 and right != 0:
            if left > right:
                result += right
            else:
                result += left
    print('#{} {}'.format(tc, result))


