def pre_order(n):
    if n > 0:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n > 0:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])

def post_order(n):
    if n > 0:
        post_order(left[n])
        post_order(right[n])
        print(n, end=' ')

import sys
sys.stdin = open('input.txt')

E = int(input())        # E개의 간선
edge = list(map(int, input().split()))

left = [0] * (E+2)      # 부모를 인덱스로 왼쪽 자식 번호 저장
right = [0] * (E+2)     # 부모를 인덱스로 오른쪽 자식 번호 저장
parent = [0] * (E+2)    # 자식을 인덱스로 부모 번호 저장
for i in range(E):
    p1, c1 = edge[i*2], edge[i*2+1]     # 부모, 자식

    if left[p1]:        # 왼쪽 자식이 있다면
        right[p1] = c1  # 부모를 인덱스로 자식 번호 저장
    else:               # 왼쪽 자식이 없으면
        left[p1] = c1   # 부모를 인덱스로 자식 번호 저장
    parent[c1] = p1     # 자식을 인덱스로 부모를 저장

root = 0

for i in range(1, E+1):
    if not parent[i]:   # 부모가 없으면
        root = i
        break

pre_order(root)         # root에서 순회 시작 (반드시 루트 노드에서 순회를 시작해야 하는 것은 아니다.)
print()
in_order(root)
print()
post_order(root)