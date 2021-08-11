import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, L-2):
        height = buildings[i]
        temp_top = 0
        for j in range(4):
            idx = [-2, -1, 1, 2]
            if buildings[i+idx[j]] > temp_top:
                temp_top = buildings[i+idx[j]]

    if height > temp_top:
        result += height - temp_top
    print('#{} {}'.format(tc, result))