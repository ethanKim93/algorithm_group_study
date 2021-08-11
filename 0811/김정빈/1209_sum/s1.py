import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    res = []

    #행열의 합
    for i in range(100):
        r = 0
        c = 0
        for j in range(100):
            r += arr[i][j]
            c += arr[j][i]
        res.append(r)
        res.append(c)

    #대각선의 합
    s1 = 0
    s2 = 0
    for i in range(100):
        s1 += arr[i][i]
        s2 += arr[i][99-i]
    res.append(s1)
    res.append(s2)

    maxV = res[0]
    for k in res:
        if k > maxV:
            maxV = k

    print('#{} {}'.format(tc, maxV))