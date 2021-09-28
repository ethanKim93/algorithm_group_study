import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def make_tree(n):
    global number
    if n <= N:
        make_tree(n * 2) # 왼쪽 노드
        tree[n] = number
        number += 1
        make_tree(n * 2 + 1) # 오른쪽 노드


for tc in range(1, T+1):
    N = int(input())

    tree = [0 for i in range(N + 1)]
    number = 1
    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))


    # 한승훈
    def inorder(n):
        global cnt
        if n <= N:
            inorder(2 * n)
            nodes[n] = cnt
            cnt += 1
            inorder(2 * n + 1)


    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        nodes = [0] * (N + 1)
        cnt = 1  # 1부터 카운트 시작
        inorder(1)
        print('#{} {} {}'.format(tc, nodes[1], nodes[N // 2]))