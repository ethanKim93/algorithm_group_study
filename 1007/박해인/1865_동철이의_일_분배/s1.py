# 순열
# import sys
# sys.stdin = open('input.txt')

def get_possibility(k, result):
    global maximum

    if result < maximum:
        return

    if result >= maximum:
        maximum = result
        return

    for i in range(N):
        result += P[k][i]
        get_possibility(k+1, result)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    maximum = 99999
    result = []

    get_possibility(0, result)

    total = 1
    for i in range(len(result)):
        total *= result[i]

    print('#{} {.6f}'.format(test_case, total*100))
