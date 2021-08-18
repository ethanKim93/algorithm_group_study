import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    pascal = []
    for i in range(1, N+1):
        pascal.append([1]*i)
    if N>=3:
        for i in range(2, N):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j]+pascal[i-1][j-1]
    print('#{}'.format(test_case))
    for k in range(N):
        print(*pascal[k])