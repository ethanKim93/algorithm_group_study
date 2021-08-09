import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    width = int(input())
    heights = list(map(int, input().split()))

    max_fall = 0
    for i in range(width):
        fall = width - 1 - i
        pile = 0
        for j in range(i+1, width):
            if heights[i] <= heights[j]:
                pile += 1

        total_fall = fall - pile
        if total_fall > max_fall:
            max_fall = total_fall

    print('#{} {}'.format(tc, max_fall))