import sys
sys.stdin = open('sample_input.txt')


def inorder(n):
    global num
    if n <= N:  # 0이 아닐 때
        inorder(n*2)
        tree[n] = num
        num += 1
        inorder(n*2+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 중위탐색 l->v->r
    tree = [0] * (N+1)
    # # 트리의 레벨 lv 찾기 - 노드 시작번호 2 ** lv
    # lv = 0
    # for i in range(0, 11):
    #     if 2 ** i <= N < 2 ** (i+1):
    #         lv = i
    #         break
    num = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

