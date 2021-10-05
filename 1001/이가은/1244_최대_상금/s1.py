import sys
sys.stdin = open('input.txt')

def max_money(money, cnt):       # type(money)=list
    global temp

    if cnt == 0:
        return money

    else:
        n = len(money)
        i=0
        while i < n - 1:
            m = i + 1
            # 뒤 쪽에서 제일 큰 값 찾기/가장 마지막 idx
            for j in range(i + 1, n):
                if money[m] <= money[j]:
                    m = j
            if money[i] < money[m]:     # 내림차순 정리
                money[i], money[m] = money[m], money[i]
                temp[int(money[i])][int(money[m])] += 1

                if :# temp에 list 같은게 2개
                    pass
                else:
                    return max_money(money, cnt-1)
            i += 1

    if len(set(money)) != len(money):       # list안에 중복되는 값이 존재하는 상태
        return max_money(money,0)

    else:
        money[n-1], money[n-2] = money[n-2], money[n-1]
        return max_money(money,cnt-1)

T = int(input())

for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    money = list(str(num))
    temp = list([0]*10 for _ in range(10))

    print('#{} {}'.format(tc, ''.join(max_money(money, cnt))))
    print(temp)

