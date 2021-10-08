import sys
sys.stdin = open('input.txt')


def function(i, max_p):
    global arr, check, total
    if i == N:
        if total < max_p:
            total = max_p
            return

    for j in range(N):
        if check[j] == 0 and total < max_p * (arr[i][j] / 100):
            check[j] = 1
            function(i + 1, max_p * (arr[i][j] / 100))
            check[j] = 0


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    total = 0
    function(0, 100)
    print('#{} {:.6f}'.format(tc, total))