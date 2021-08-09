import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    width = int(input())
    heights = list(map(int, input().split()))
    # print(width)
    max_gap = 0
    for x_l in range(width-1):
        gap = 0
        for x_r in range(x_l+1, width):
            if heights[x_l] > heights[x_r]:
                gap += 1
            else:
                pass
        if gap > max_gap:
            max_gap = gap
    print('#{} {}'.format(tc, max_gap))

