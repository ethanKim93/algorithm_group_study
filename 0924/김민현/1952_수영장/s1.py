import sys
sys.stdin = open("sample_input.txt", "r")


# cost : 이전 달까지의 계산 결과, m 현재 내가 보낼 결과
def calc(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    # # 1일권
    # calc(cost + d * month[m], m + 1)
    # # 1달권
    # calc(cost + m1, m + 1)

    calc(cost + min(d * month[m], m1), m + 1)
    # 3달권
    calc(cost + m3, m + 3)


T = int(input())

for tc in range(1, T + 1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    min_cost = y  # 1년치 비용이 현재 최저의 가격

    calc(0, 1)
    print("#{} {}".format(tc, min_cost))

