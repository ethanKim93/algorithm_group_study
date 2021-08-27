import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))

    key = 1
    cnt = 1
    while True:
        if not key:
            key = 1
            cnt += 1
        temp = arr.pop(0) - key
        if temp <= 0:
            temp = 0
            arr.append(temp)
            break
        arr.append(temp)
        key = (key + 1) % 6
    print('#{} '.format(tc), end='')
    print(*arr, sep=' ')