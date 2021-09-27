import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    price = list(map(int, input().split()))
    use = list(map(int, input().split()))
    fee = list([0]*12)

    for i in range(len(use)):
        if i == 0 :
            tmp0 = use[i] * price[0]
            tmp1 = price[1]
            if tmp0 > tmp1: fee[i] = tmp1
            else: fee[i] = tmp0

        if i == 1:
            tmp0 = fee[0] + use[i] * price[0]
            tmp1 = fee[0] + price[1]
            if tmp0 > tmp1:fee[i] = tmp1
            else:fee[i] = tmp0

        if i == 2:
            tmp0 = fee[1] + use[i] * price[0]
            tmp1 = fee[1] + price[1]
            tmp2 = price[2]
            fee[2] = min(tmp0, tmp1, tmp2)

        if i >= 3:
            tmp0 = fee[i-1] + use[i] * price[0]
            tmp1 = fee[i-1] + price[1]
            tmp2 = fee[i-3] + price[2]
            fee[i] = min(tmp0, tmp1, tmp2)

        if i == 11:
            if fee[-1] > price[-1]: fee[-1] = price[-1]

    print('#{} {}'.format(tc, fee[-1]))