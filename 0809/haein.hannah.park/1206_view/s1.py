import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input()) #길이
    buildings = list(map(int, input().split()))

    # 조망권이 확보 된 빌딩 : goodbuilding
    goodbuilding = 0
    for b in range(2, L-2):
        r1 = buildings[b+1]
        r2 = buildings[b+2]
        l1 = buildings[b-1]
        l2 = buildings[b-2]
        # 주변 가장 큰 빌딩 높이 체크
        tallest = max(r1, r2, l1, l2)
        if buildings[b] > tallest:
            goodbuilding += buildings[b] - tallest

    print('#{} {}'.format(tc, goodbuilding))




