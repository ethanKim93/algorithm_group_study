import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    max_drop = 0

    for i in range(N-1):
        now = heights[i]
        parts = heights[i+1:]
        drop = 0
        for idx in range(len(parts)):
            if now > parts[idx]:
                drop += 1
        if max_drop < drop:
            max_drop = drop

    print('#{} {}'.format(tc, max_drop))