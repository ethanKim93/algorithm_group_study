import sys
sys.stdin = open("input.txt")

T = int(input())
for test in range(T):

    pas_n = int(input())
    pas_arr = [[1]* i for i in range(1, pas_n+1)]

    if pas_n > 2:
        for i in range(2, pas_n):
            for j in range(i-1):
                pas_arr[i][j+1] = pas_arr[i-1][j] + pas_arr[i-1][j+1]

    print('#{}'.format(test+1))
    for arr in pas_arr:
        print(*arr)