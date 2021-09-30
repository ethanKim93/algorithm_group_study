import sys
sys.stdin = open('sample_input.txt')


def heap(i):
    while i//2 and tree[i//2] > tree[i]:
        tree[i//2], tree[i] = tree[i], tree[i//2]
        i //= 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [0] + list(map(int, input().split()))
    tree = [0] * (N + 1)
    total = 0

    for i in range(1, len(num_list)):
        tree[i] = num_list[i]
        heap(i)

    while N:
        total += tree[N//2]
        N //= 2
    print('#{} {}'.format(tc, total))


