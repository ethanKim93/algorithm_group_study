import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    money = int(input())

    result = []
    i = 0
    cnt = 0
    while cnt < 8:
        if i == 0:
            if int(money) // 50000 != 0:
                a = int(money) // 50000
                result.append(a)
                money = int(money) - (50000 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 50000)
                i += 1
                cnt += 1
        if i == 1:
            if int(money) // 10000 != 0:
                a = int(money) // 10000
                result.append(a)
                money = int(money) - (10000 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 10000)
                i += 1
                cnt += 1
        if i == 2:
            if int(money) // 5000 != 0:
                a = int(money) // 5000
                result.append(a)
                money = int(money) - (5000 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 5000)
                i += 1
                cnt += 1
        if i == 3:
            if int(money) // 1000 != 0:
                a = int(money) // 1000
                result.append(a)
                money = int(money) - (1000 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 1000)
                i += 1
                cnt += 1
        if i == 4:
            if int(money) // 500 != 0:
                a = int(money) // 500
                result.append(a)
                money = int(money) - (500 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 500)
                i += 1
                cnt += 1
        if i == 5:
            if int(money) // 100 != 0:
                a = int(money) // 100
                result.append(a)
                money = int(money) - (100 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 100)
                i += 1
                cnt += 1
        if i == 6:
            if int(money) // 50 != 0:
                a = int(money) // 50
                result.append(a)
                money = int(money) - (50 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 50)
                i += 1
                cnt += 1
        if i == 7:
            if int(money) // 10 != 0:
                a = int(money) // 10
                result.append(a)
                money = int(money) - (10 * a)
                i += 1
                cnt += 1
                a = 0
            else:
                result.append(int(money) // 10)
                i += 1
                cnt += 1

    print('#{}'.format(tc))
    print(*result)
