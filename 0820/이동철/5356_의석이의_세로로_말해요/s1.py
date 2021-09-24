import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]

    max_length = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_length:
            max_length = len(arr[i])

    result = ''
    for i in range(max_length):
        for j in range(5):
            try:
                result += arr[j][i]
            except:
                continue

    print('#{} {}'.format(tc, result))