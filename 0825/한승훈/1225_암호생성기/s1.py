import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    data = list(map(int, input().split()))
    i = 1
    while data[-1]:
        k = data.pop(0) - i
        if k <= 0:
            k = 0
        data.append(k)
        i += 1
        if i == 6:
            i = 1

    print('#{} '.format(tc), end='')
    print(*data)