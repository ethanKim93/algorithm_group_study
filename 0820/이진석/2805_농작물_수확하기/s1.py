import sys

sys.stdin = open('input.txt')
for tc in range(1, int(input()) + 1):
    N = int(input())
    table = []
    for i in range(N):
        arr = list(map(int, list(input())))
        table.append(arr)
    result = 0

    middle = left = right = N//2
    for i in range(N):
        for j in range(left, right+1):
            result += table[i][j]
        if i < middle:  # 0 ~ N//2 까지
            left -= 1
            right += 1
        else:           # N//2 ~ N 까지
            left += 1
            right -= 1
    print('#{} {}'.format(tc, result))