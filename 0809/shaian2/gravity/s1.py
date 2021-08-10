import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    width = int(input())
    heights = list(map(int, input().split()))
    total = ''
    for height in heights:
        if height:
            total += str(height)
    print('#{} {}'.format(tc, total))
    # f-string 안됨
