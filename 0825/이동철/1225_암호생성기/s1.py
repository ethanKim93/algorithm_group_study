import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))

    num = 1

    while True:
        flag = 0
        for i in range(len(arr)):
            arr[i] -= num
            num += 1
            if num > 5:
                num = 1
            if arr[i] <= 0:
                arr[i] = 0
                flag = 1
                break
        if flag:
            break
    while arr[-1] != 0:
        arr.insert(0, arr.pop())

    print('#{}'.format(tc), *arr)

