import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    height = int(input())

    list_a = [[0]*height for _ in range(height)]

    for i in range(height):
        list_a[i][0] = 1

    for i in range(1, height):
        for j in range(1, i+1):
            list_a[i][j] = list_a[i-1][j-1] + list_a[i-1][j]

    print('#{}'.format(tc))
    for i in range(height):
        for j in range(height):
            if list_a[i][j] != 0:
                print(list_a[i][j], end=' ')
        print()

