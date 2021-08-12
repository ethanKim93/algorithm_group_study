import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for case in range(T):
    N, K = map(int, input().split())

    total = 0
    for i in range(1, 1 << 12):
        sum_val = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                sum_val += j + 1
                cnt += 1
        if cnt == N and sum_val == K:
            total += 1

    print("#{} {}".format(case + 1, total))