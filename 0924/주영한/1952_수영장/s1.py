import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    days, months, three_months, years = map(int, input().split())

    tables = [0, 0] + list(map(int, input().split()))
    dp = [0] * 14

    dp[2] = min(tables[2] * days, months, three_months)

    for idx in range(3, 14):
        dp[idx] = min(dp[idx - 1] + tables[idx] * days, dp[idx - 1] + months, dp[idx - 3] + three_months)
    print("#{} {}".format(tc, min(dp[13], years)))