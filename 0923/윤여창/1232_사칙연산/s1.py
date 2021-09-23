import sys

sys.studin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    nd = [[0]] + [list(input().split()) for _ in range(n)]
    arr = [[0, 0, 0] for _ in range(n + 1)]

    for q in range(n + 1):
        if len(nd[q]) == 4:
            idx, car, left, right = nd[q]
            arr[q][2] = car
            arr[int(left)][0] = q
            arr[int(right)][0] = q
        elif len(nd[q]) == 3:
            idx, num = nd[q]
            arr[q][1] = int(num)

    for w in range(n // 2):
        if arr[arr[n - 2 * w - 1][0]][2] == '+':
            arr[arr[n - 2 * w - 1][0]][1] = arr[n - 2 * w - 1][1] + arr[n - 2 * w][1]

        elif arr[arr[n - 2 * w - 1][0]][2] == '-':
            arr[arr[n - 2 * w - 1][0]][1] = arr[n - 2 * w - 1][1] - arr[n - 2 * w][1]

        elif arr[arr[n - 2 * w - 1][0]][2] == '*':
            arr[arr[n - 2 * w - 1][0]][1] = arr[n - 2 * w - 1][1] * arr[n - 2 * w][1]

        else:
            arr[arr[n - 2 * w - 1][0]][1] = arr[n - 2 * w - 1][1] / arr[n - 2 * w][1]

    print('#{} {}'.format(tc, int(arr[1][1])))