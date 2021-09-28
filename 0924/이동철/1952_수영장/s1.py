import sys
sys.stdin = open('sample_input.txt')


# cost : 이전 달까지의 계산 결과, date 현재 내가 보낼 결과
def calculate(cost, date):
    global min_cost

    if date > 12:
        if min_cost > cost:
            min_cost = cost
        return
    # 1일권
    calculate(cost + day * plan[date], date + 1)
    # 1달권
    calculate(cost + one_month, date + 1)

    # calculate(cost + min(d * plan[date], one_month), date + 1)

    # 3달권
    calculate(cost + three_month, date + 3)


T = int(input())

for tc in range(1, T + 1):
    day, one_month, three_month, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    min_cost = year
    # 1년치 비용이 현재 최저의 가격

    calculate(0, 1)

    print('#{} {}'.format(tc, min_cost))


##############################################

# T = int(input())
#
# for tc in range(1, T + 1):
#     day, one_month, three_month, year = map(int, input().split())
#     plan = [0] + list(map(int, input().split()))
#
#     dp = [0] * 13  # 해당 월까지의 최소값이 저장이 되어있음
#
#     dp[1] = min(one_month, plan[1] * day)
#     dp[2] = dp[1] + min(one_month, plan[2] * day)
#
#     for i in range(3, 13):
#         dp[i] = min(dp[i - 3] + three_month, dp[i - 1] + one_month, dp[i - 1] + plan[i] * d)
#
#     print("#{} {}".format(tc, min(dp[12], y)))
