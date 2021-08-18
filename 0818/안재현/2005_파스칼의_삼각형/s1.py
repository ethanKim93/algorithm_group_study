import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(0 , T):
    N = int(input())

    triangle = [[1] * x for x in range(1, N+1)]

    for i in range(1, N-1):
        for j in range(len(triangle[i])-1):
            triangle[i+1][j+1] = triangle[i][j] + triangle[i][j+1]

    print("#{}".format(tc + 1))
    for p in range(len(triangle)):
        result = triangle[p]
        for k in range(len(result)):
            print(str(result[k]), end=' ')
        print()