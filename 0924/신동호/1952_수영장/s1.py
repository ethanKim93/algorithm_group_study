import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 13
    for ind, val in enumerate(plan, start=1):
        if ind < 3:
            if plan[ind-1] * day > mon:
                dp[ind] = dp[ind-1] + mon
            else:
                dp[ind] = dp[ind-1] + plan[ind-1] * day
        else:
            if dp[ind-3] + mon3 < dp[ind-1] + mon and dp[ind-3] + mon3 < dp[ind-1] + plan[ind-1] * day:
                dp[ind] = dp[ind-3] + mon3
            elif plan[ind-1] * day > mon:
                dp[ind] = dp[ind-1] + mon
            else:
                dp[ind] = dp[ind - 1] + plan[ind-1] * day
    if dp[12] > year:
        print('#{} {}'.format(tc, year))
    else:
        print('#{} {}'.format(tc, dp[12]))
