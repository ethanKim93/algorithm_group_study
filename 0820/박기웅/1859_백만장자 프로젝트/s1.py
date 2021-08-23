import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    costs = list(map(int, input().split()))
    maxc = costs[-1]
    gain = 0

    for c in costs[::-1]:
        if c > maxc:
            maxc = c
        else:
            gain += maxc - c
    print('#{} {}'.format(tc, gain))

