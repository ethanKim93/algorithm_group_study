import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    L = int(input())
    buildings = list(map(int,input().split()))
    tot = 0
    for b_x in range(2,L-2):
        max_b = buildings[b_x - 2]
        for i in [-1, 1, 2]:
            if max_b < buildings[b_x + i]:
                max_b = buildings[b_x + i]
        if buildings[b_x] > max_b:
            tot += (buildings[b_x] - max_b)
    print('#{} {}'.format(tc, tot))