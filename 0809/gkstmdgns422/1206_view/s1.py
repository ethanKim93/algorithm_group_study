import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    ans = 0
    i = 2
    while i < L-2:

        if buildings[i-2] >= buildings[i] or buildings[i-1] >= buildings[i] or buildings[i+1] >= buildings[i]:
            i += 1

        elif buildings[i+2] >= buildings[i]:
            i += 2

        else:
            nearby = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
            max_num = 0
            for num in nearby:
                if num > max_num:
                    max_num = num
            ans += buildings[i] - max_num
            i += 3
    print('#{} {}'.format(tc,ans))





