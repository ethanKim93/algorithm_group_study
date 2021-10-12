money_set = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T + 1):
    money = int(input())
    cnt_list = [0] * len(money_set)
    for i in range(len(money_set)):
        cnt_list[i] = money // money_set[i]
        money = money % money_set[i]
    print("#{}".format(tc))
    print(*cnt_list)