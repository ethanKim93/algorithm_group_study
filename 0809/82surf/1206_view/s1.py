import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, L-1):
        gaps = [0, 0, 0, 0]
        gaps[0] = buildings[i] - buildings[i-2]
        if gaps[0] <= 0:
            continue
        gaps[1] = buildings[i] - buildings[i-1]
        if gaps[1] <= 0:
            continue
        gaps[2] = buildings[i] - buildings[i+1]
        if gaps[2] <= 0:
            continue
        gaps[3] = buildings[i] - buildings[i+2]
        if gaps[3] <= 0:
            continue

        min_gap = gaps[0]
        for gap in gaps:
            if gap < min_gap:
                min_gap = gap
            else:
                pass

        result += min_gap
    print('#{} {}'.format(tc, result))