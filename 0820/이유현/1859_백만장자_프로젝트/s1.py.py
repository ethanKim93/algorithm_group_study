T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    price = price[::-1]
    maxp = price[0]
    bf = 0
    for i in range(1, len(price)):
        if maxp > price[i]:
            bf += maxp - price[i]
        else:
            maxp = price[i]
    print('#{} {}'.format(tc, bf))
    # s1   
    # bf = 0
    # buy = 0
    # cnt = 0
    # for i in range(N-1):
    #     if p[i] > p[i+1]:
    #         for p_high in p[i+2:]:
    #             if p_high > p[i]:
    #                 buy += p[i]
    #                 cnt += 1
    #                 break
    #         else:
    #             bf += p[i] * cnt - buy
    #             print(buy, cnt)
    #             buy = 0
    #             cnt = 0
                   

    #     elif p[i] < p[i+1]:
    #         buy += p[i]
    #         cnt += 1
    
    #     elif p[i] == p[i+1]:
    #         for p_high in p[i+2:]:
    #             if p_high > p[i]:
    #                 buy += p[i]
    #                 cnt += 1
    #                 break
    #         continue
    
    # bf += p[N-1] * cnt - buy

    # print('#{} {}'.format(tc, bf))


    '''
    1) 사야하나? 팔아야하나? 마지막 날은 고려하지 않는다(그날사서 그날팔면 0이니까)
    반복을 순회하다가 나보다 큰값이 있으면 바꾸고 없으면 유지, 반복을 엄청 돌아야한다
    2) 팔 수 있는지 없는지 체크
    현재지점보다 나중에 더 큰값이 있는지 체크, 
    물건개수 가격개수 반복문 돌면서 카운트, 큰 값을 만나면(큰값*개수 - 산 가격들)
    3) 반대로 생각을 해보자
    가격을 알고있기 때문에 마지막 값을 최고값이라고 가정
    앞으로 가면서 나보다 작으면 차이를 이익에 더해줌
    나보다 큰값을 만나면 최고값을 갱신, 다시 앞으로 가면서 이익을 계산한다
    '''