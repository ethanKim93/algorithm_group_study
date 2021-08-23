T = int(input())

for i in range(T):
    profit = 0
    days = input()
    costs = list(map(int,input().split(" ")))
    #print(max(costs))
    start = end = 0
    while start < len(costs):
        max_price = max(costs[start:])
        end = costs[start:].index(max_price) + start #찾은 값과 같은 값이 있음에 주의
        cnt = len(costs[start:end])
        profit += cnt * max_price - sum(costs[start:end])
        start = end + 1
    print(f"#{i + 1} {profit}")