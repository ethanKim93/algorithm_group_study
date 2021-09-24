import sys

sys.stdin = open('sample_input.txt')
T = int(input())

def sub_tree(n):
    global cnt, tree
    if tree.get(n):
        for j in tree[n]:
            cnt += 1
            if tree.get(j):
                sub_tree(j)


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = {}

    for i in range(E):
        if tree.get(nodes[2*i]):  # 자식 노드가 존재 하는지 여부확인
            tree[nodes[2*i]] = tree[nodes[2*i]] + [nodes[2*i+1]]  # 리스트 형태로 저장했기에 +로 추가
        else:
            tree[nodes[2*i]] = [nodes[2*i+1]]
    cnt = 1  # 루트 노드 포함
    sub_tree(N)

    print('#{} {}'.format(tc, cnt))

