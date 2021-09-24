import sys
sys.stdin = open('input.txt')


def deg90(arr):
    re_arr = ''
    result = []
    for i in range(N):
        for j in range(N):
            re_arr += arr[N - 1 - j][i]
            if len(re_arr) == N:
                result.append(re_arr)
                re_arr = ''
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    a = deg90(arr)
    b = deg90(a)
    c = deg90(b)

    print("#{}".format(tc))
    for i in range(N):
        print(a[i], b[i], c[i])
