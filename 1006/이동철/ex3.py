'''
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre_order(n):
    if n:
        # 유효한 정점이면
        print(n)
        pre_order(left[n])
        pre_order(right[n])


def inorder_order(n):
    if n:
        pre_order(left[n])
        print(n)
        pre_order(right[n])


def post_order(n):
    if n:
        pre_order(left[n])
        pre_order(right[n])
        print(n)


V = int(input())
edge = list(map(int, input().split()))

E = V - 1
# V개의 정점이 있는 트리의 간선 수

left = [0] * (V + 1)
right = [0] * (V + 1)
# 부모를 인덱스로 자식번호 저장

parent = [0] * (V + 1)
# 자식을 인덱스로 부모번호 저장

for i in range(E):
    p, c = edge[i * 2], edge[i * 2 + 1]
    if left[p] == 0:
        # p의 왼쪽자식이 없으면
        left[p] = c
    else:
        # 왼쪽자식이 있으면 오른쪽자식으로 저장
        right[p] = c
    parent[c] = p


pre_order(1)
inorder_order(1)
post_order(1)


# 건희님 풀이
# def preorder(start):
#     if not start:
#         return
#
#     print(start, end=" ")
#     preorder(left[start])
#     preorder(right[start])
#
# def inorder(start):
#     if not start:
#         return
#
#     inorder(left[start])
#     print(start, end=" ")
#     inorder(right[start])
#
# def postorder(start):
#     if not start:
#         return
#
#     postorder(left[start])
#     postorder(right[start])
#     print(start, end=" ")
#
#
# v = int(input())
# maps = list(map(int,input().split()))
#
# left = [0]*(v+1)
# right = [0]*(v+1)
#
# for i in range(0,len(maps),2):
#     if not left[maps[i]]:
#         left[maps[i]] = maps[i+1]
#     else:
#         right[maps[i]] = maps[i+1]
#
# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)