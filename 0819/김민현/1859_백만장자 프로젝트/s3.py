import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    cost = list(map(int,input().split())) # 가격들을 입력을 받았다

    ans = 0
    # 첫번째 방법
    # for i in range(N-1): #마지막 날은 안사도 그만
    #     max_cost = cost[i]
    #     for j in range(i+1,N):
    #         if max_cost < cost[j]:
    #             max_cost = cost[j]
    #
    #     if max_cost > cost[i]:
    #         ans += max_cost-cost[i] #이익을 구하자
    #
    #     print('#{} {}'.format(tc, ans))


    #두번째 방법
    # is_sell = [False] * N
    #
    # for i in range(N-1):
    #     for j in range(i+1,N):
    #         if cost[i] < cost[j]:
    #             is_sell[i] = True
    #             break
    # buy_cost = 0
    # buy_cnt = 0
    #
    # for i in range(N):
    #     if is_sell[i]:
    #         buy_cost += cost[i]
    #         buy_cnt += 1
    #     else:
    #         ans += (cost[i]*buy_cnt) = buy_cost
    #         buy_cost = 0
    #         buy_cnt = 0
    #
    # print('#{} {}'.format(tc, ans))

    #세번째 방법 (반대로 생각)

    max_cost = cost[-1]

    for i in range(N-2,-1,-1):
        # 내가 가진 값보다 보고 있는 값이 작을때
        if max_cost> cost[i]:
            ans += max_cost = cost[i]
        else:
            max_cost = cost[i]
    print('#{} {}'.format(tc, ans))