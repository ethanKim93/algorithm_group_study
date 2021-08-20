#1859. 백만 장자 프로젝트
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int,input().split()))
    sell = price[-1]
    res = 0
    for p in price[-1::-1]:
        if p < sell:
            res += sell - p
        elif p >= sell:
            sell = p

    print('#{} {}'.format(tc, res))