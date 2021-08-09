import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, L - 2):
        if buildings[i - 1] < buildings[i] and buildings[i - 2] < buildings[i] and buildings[i + 1] < buildings[i] and buildings[i + 2] < buildings[i] :
            list_gap = []
            list_gap.append(buildings[i] - buildings[i - 2])
            list_gap.append(buildings[i] - buildings[i - 1])
            list_gap.append(buildings[i] - buildings[i + 1])
            list_gap.append(buildings[i] - buildings[i + 2])
            gap_min = list_gap[0]
            for gap in list_gap:
                if gap < gap_min:
                    gap_min = gap
            cnt += gap_min
    print('#{} {}'.format(tc, cnt))
