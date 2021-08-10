import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_total = min_total = 0

    for i in range(0, N - M + 1):
        total = 0
        for j in range(M):
            total += nums[i + j]

        if i == 0:
            max_total = total
            min_total = total
            continue

        if max_total < total:
            max_total = total
        if min_total > total:
            min_total = total

    print("#{} {}".format(case + 1, max_total - min_total))
