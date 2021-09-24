import sys
sys.stdin = open('sample_input.txt')


def search(n):
    global cnt
    if n <= N:
        search(n*2)
        tree[n] = cnt
        cnt += 1
        search(n*2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    search(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
