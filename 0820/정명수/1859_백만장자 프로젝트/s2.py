ans = 0
is_sell = [False] * N
for i in range(N-1):
    for j in range(i+1,N):
        if cost[i] < cost[j]:
            is_sell[i] = True
buy_cost = 0
buy_cnt = 0

for i in range(N):
    if is_sell[i]:
        buy_cost += cost[i]
        buy_cnt += 1
    else:
        ans += (cost[i]*buy_cnt) - buy_cost
        buy_cost = 0
        buy_cnt = 0
print()