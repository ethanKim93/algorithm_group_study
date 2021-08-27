import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())  # 사람/붕어빵수/per
    arrive = sorted(list(map(int, input().split())))
    # print('{}개 / {}초'.format(K, M))

    flag = 'Possible'
    tab = 0
    for arr in arrive:
        tib = (arr//M)*K
        stock = tib - tab
        if stock <= 0:
            flag = 'Impossible'
            break
        else:
            tab += 1
    print('#{} {}'.format(tc, flag))