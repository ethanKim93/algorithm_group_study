import sys

sys.stdin = open('sample_input.txt')


def make_tree(n):  # 완전 이진 트리의 left,right 작성
    for i in range(1, n - 2):
        if i * 2 <= n:
            l[i] = i * 2
        if i * 2 + 1 <= n:
            r[i] = i * 2 + 1

def in_order(n):  # 중위순회(LVR) 하면서 1부터 오름차순으로 정렬 된 값 입력
    global value
    if n:
        in_order(l[n])
        complete_tree[n] = value
        value += 1
        in_order(r[n])


for tc in range(1, int(input()) + 1):
    N = int(input())
    complete_tree = [0] * (N + 1)  # 완전 이진 트리
    l = [0] * (N + 1)  # 완전 이진 트리 left
    r = [0] * (N + 1)  # right
    value = 1  # 이진 탐색 트리에 저장할 값

    make_tree(N)
    print(l)
    print(r)
    in_order(1)
    print('#{} {} {}'.format(tc, complete_tree[1], complete_tree[N // 2]))
    # 루트에 저장된 값 : 완전 이진트리의 1번노드,  N/2번 노드에 저장된 값 : N // 2번 노드