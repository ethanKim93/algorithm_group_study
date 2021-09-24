import sys
sys.stdin = open('sample_input.txt')


def heap(n):
    if n > 0:
        if nodes[n//2] > nodes[n]:
            nodes[n], nodes[n//2] = nodes[n//2], nodes[n]
            heap(n//2)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = [0] + list(map(int, input().split()))
    for node in range(1, len(nodes)):
        heap(node)
    ans = 0
    while N:
        N //= 2
        ans += nodes[N]
    print('#{} {}'.format(tc, ans))
