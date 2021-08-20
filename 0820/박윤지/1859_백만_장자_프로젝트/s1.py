import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    result = 0
    maxV = price[-1]
    for i in price[N-1::-1]:
        if i <= maxV:
            result += maxV - i
        else:
            maxV = i

    print('#{} {}'.format(tc, result))


'''
# 재귀라서 Runtime error 나오는듯
def calc(price, result):
    while len(price) != 0:
        # 최고가 value, index 구하기
        maxV = 0
        maxIdx = 0
        for i in range(len(price)):
            if price[i] > maxV:
                maxV = price[i]
                maxIdx = i

        for j in range(maxIdx):
            result += (maxV - price[j])
        return calc(price[maxIdx+1:], result)
    else:
        return result
'''