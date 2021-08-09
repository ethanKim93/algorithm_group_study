import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    view = 0
    for i in range(2, L-2):
        H = buildings[i-2]
        if H < buildings[i-1]:
            H = buildings[i-1]
        if H < buildings[i+1]:
            H = buildings[i+1]
        if H < buildings[i+2]:
            H = buildings[i+2]
        if buildings[i] > H:
            view += buildings[i] - H

    print('#{} {}'.format(tc, view))