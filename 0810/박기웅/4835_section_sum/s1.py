import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    i = sumMin = sumMax = 0
    for _ in range(M):
        sumMin += nums[_]
        sumMax += nums[_]

    while (i <= N-M):
        sumM = 0
        for idx in range(i, i+M):
            sumM += nums[idx]

        if sumM > sumMax:
            sumMax = sumM
        if sumM < sumMin:
            sumMin = sumM

        i += 1

    print('#{} {}'.format(tc, sumMax-sumMin))


