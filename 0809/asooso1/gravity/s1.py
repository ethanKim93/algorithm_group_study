import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T + 1):
    width = int(input())
    heights = list(map(int, input().split()))
    max_down = 0
    for i in range(width - 1):
        temp = width - i - 1
        for j in range(i + 1, width):
            if heights[i] <= heights[j]:
                temp -= 1
        if temp > max_down:
            max_down = temp
    print('#{} {}'.format(testcase, max_down))
