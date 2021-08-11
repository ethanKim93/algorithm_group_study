import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    abs_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for a,b in [[-1,0],[0,1],[1,0],[0,-1]]:
                if 0 <= i+a < 5 and 0 <= j+b < 5:
                    abs_sum += abs(arr[i+a][j+b]-arr[i][j])
    print(abs_sum)

