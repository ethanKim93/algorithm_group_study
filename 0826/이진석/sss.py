import sys
sys.stdin = open('input.txt')


def new_operator(num):
    temp = 0
    pair = []
    for n in range(0, 2000):
        if (n*(n+1)//2) <= num <= ((n+1)*(n+2)//2):
            pair = [n+1, 1]
            temp = ((n+1)*(n+2))//2

    while num != temp:
        pair[0] -= 1
        pair[1] += 1
        temp -= 1
    result = [pair[0], pair[1]]

    return result


def operator(a, b):
    num = (a ** 2 + a) // 2 + a * (b - 1) + (b - 2) * (b - 1) // 2

    return num


T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    a = new_operator(x)
    b = new_operator(y)

    p = [a[0] + b[0], a[1] + b[1]]
    print(p)
    q = operator(p[0], p[1])
    # print(q)
