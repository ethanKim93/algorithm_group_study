import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dumps = int(input())
    heights = list(map(int, input().split()))
    for dump in range(dumps + 1):
        max_idx = 0
        min_idx = 0
        for idx in range(100):
            if heights[idx] > heights[max_idx]:
                max_idx = idx
        for idx in range(100):
            if heights[idx] < heights[min_idx]:
                min_idx = idx
        if dump != dumps:
            heights[max_idx] -= 1
            heights[min_idx] += 1
    print('#{} {}'.format(tc, heights[max_idx] - heights[min_idx]))

