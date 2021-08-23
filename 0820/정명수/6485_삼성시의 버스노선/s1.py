import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number = []
    for _ in range(N):
        a, b = map(int, input().split())
        number.append([a, b])
    P = int(input())
    station = [0] * 5001
    check = []
    for _ in range(P):
        k = int(input())
        check.append(k)

    for region in number:
        for i in range(region[0], region[1] + 1):
            station[i - 1] += 1
    print('#{}'.format(tc), end=" ")
    for j in check:
        if j == check[-1]:
            print(station[j - 1])
        else:
            print(station[j - 1], end=" ")