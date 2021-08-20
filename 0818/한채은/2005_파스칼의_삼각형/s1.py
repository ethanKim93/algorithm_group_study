import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = []

    for i in range(1, N+1):
        num.append([1] * i)

    for i in range(0, N):
        if i >= 2:
            for j in range(1, len(num[i])-1):
                num[i][j] = num[i-1][j] + num[i-1][j-1]

    print("#{}".format(tc))

    for i in range(N):
        print(*num[i])
