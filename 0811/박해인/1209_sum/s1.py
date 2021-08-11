import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # diagonal
    s1 = 0
    s2 = 0
    for i in range(100):
        s1 += arr[i][i]  # right
        s2 += arr[i][99-i]  # left
    maxV = s1

    if maxV < s2:
        maxV = s2

    # row, column total
    for i in range(100):
        s1 = 0
        s2 = 0
        for j in range(100):
            s1 += arr[i][j] #row
            s2 += arr[j][i] #column
        if maxV < s1:
            maxV = s1
        if maxV < s2:
            maxV = s2

    print('#{} {}'.format(test_case, maxV))

