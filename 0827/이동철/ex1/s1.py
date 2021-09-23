import sys
sys.stdin = open('input.txt')


#전위
def pre_order(n):
    if n:
        # 유효한 정점이라면
        print(n, end=' ')
        pre_order(left[n])  # n의 왼쪽 자식으로 접근
        pre_order(right[n]) # n의 오른쪽 자식으로 접근


#중위
def inorder_traverse(n):
    if n:
        # 유효한 정점이라면
        inorder_traverse(left[n])  # n의 왼쪽 자식으로 접근
        print(n, end=' ')
        inorder_traverse(right[n]) # n의 오른쪽 자식으로 접근


#후위
def posterorder_traversal(n):
    if n:
        posterorder_traversal(left[n])  # n의 왼쪽 자식으로 접근
        posterorder_traversal(right[n])  # n의 오른쪽 자식으로 접근
        print(n, end=' ')


V = int(input())
# 트리의 정점의 총 개수
edge = list(map(int, input().split()))
# 간선의 정보
E = V -1
# 간선 개수
left = [0] * (V + 1)
right = [0] * (V + 1)
# 부모의 인덱스로 왼쪽 오른쪽 자식을 나눠서 자식번호 저장
for i in range(E):
    p, c = edge[i * 2], edge[(i * 2) + 1]
    # p = parent c = child
    if left[p] == 0:
        # p의 왼쪽 자식이 없으면
        left[p] = c
    else:
        # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c


# pre_order(1)
# inorder_traverse(1)
posterorder_traversal(1)
