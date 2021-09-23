import sys

sys.stdin = open('input.txt')


# 중위 순회
def in_order(v):
    if v:
        print(v)
        print(type(v))
        in_order(left[int(v)])
        print(N_list[int(v)], end="")
        in_order(right[int(v)])


for tc in range(10):
    T = int(input())
    left = [0]*(T+1)
    right = [0]*(T+1)
    N_list = [0] * (T + 1)
    for i in range(1, T + 1):
        N = list(input().split())
        N_list[i] = N[1]
        if len(N) >= 3:
            left[i] = N[2]
        if len(N) == 4:
            right[i] = N[3]

    print('#{} '.format(tc + 1), end='')
    in_order(1)
    print()