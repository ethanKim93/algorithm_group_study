import sys
sys.stdin = open('sample_input.txt')


def inorder(n):
    global cnt
    if n <= N:
        inorder(2*n)
        nodes[n] = cnt
        cnt += 1
        inorder(2*n + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = [0] * (N+1)
    cnt = 1  # 1부터 카운트 시작
    inorder(1)
    print('#{} {} {}'.format(tc, nodes[1], nodes[N//2]))
