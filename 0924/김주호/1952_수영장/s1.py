def purchase(month=0, now_cost=0):
    if month >= 12:
        global total_cost
        if total_cost > now_cost:
            total_cost = now_cost
        return

    cost_days = plan[month] * cost_day

    cost = cost_days if cost_days < cost_month else cost_month
    purchase(month + 1, now_cost + cost)
    purchase(month + 3, now_cost + cost_3month)


for case in range(int(input())):
    cost_day, cost_month, cost_3month, cost_year = map(int, input().split())
    plan = list(map(int, input().split()))

    total_cost = 3000 * 400
    purchase()

    print("#{} {}".format(case + 1, total_cost if total_cost < cost_year else cost_year))
