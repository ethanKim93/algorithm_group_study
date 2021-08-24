import sys
sys.stdin = open('sample_input.txt')


def f(idx, N):
    global min_total
    if idx == N:
        for i in range(N):
            if bit.count(bit[i]) != 1:
                return
        total = 0
        for i in range(N):
            total += arr[i][bit[i]]
        if min_total > total:
            min_total = total
        # print(total, min_total)
    else:
        # subsum = 0
        # for i in range(idx):
        #     subsum += arr[i][bit[idx]]
        # print(subsum)
        # if min_total > subsum:
            for i in range(N):
                bit[idx] = i
                f(idx+1, N)
            # print(bit)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    min_total = 31
    f(0, N)
    print('#{} {}'.format(tc, min_total))