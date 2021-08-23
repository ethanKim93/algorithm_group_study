import sys
sys.stdin = open('input.txt', 'r')

def abs_val(n):
    if n < 0:
        return -n
    return n

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [input() for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if j >= abs_val(N//2 - i) and j < N - abs_val(N//2 - i):
                result += int(farm[i][j])

    print("#{} {}".format(tc, result))