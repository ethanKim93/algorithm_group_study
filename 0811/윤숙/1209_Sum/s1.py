import sys
sys.stdin=open('input.txt')
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV=0

    s=0

    for i in range(100):
        s=0
        s+=arr[i][i]

        if maxV < s:
            maxV = s

    for i in range(100):
        s=0
        s+=arr[i][99-i]

        if maxV < s:
            maxV = s

    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]

        if maxV < s:
            maxV = s

    for j in range(100):
        s = 0
        for i in range(100):
            s += arr[i][j]
        if maxV < s:
            maxV = s

    print('#{} {}'.format(tc,maxV))
