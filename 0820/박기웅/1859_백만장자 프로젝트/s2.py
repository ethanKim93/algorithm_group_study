import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    costs = list(map(int, input().split()))
    maxc = costs[-1]
    gain = 0
    for i in costs[::-1]:
        if maxc > i:
            gain += maxc - i
        else:
            maxc = i

    print('#{} {}'.format(test_case, gain))