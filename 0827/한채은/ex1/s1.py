import sys
sys.stdin = open('input.txt')

# 전위 순회
def preorder(n):
    if n:
        print(n, end=" ")
        preorder(left[n])
        preorder(right[n])

# 중위 순회
def inorder(n):
    if n:
        preorder(left[n])
        print(n, end=" ")
        preorder(right[n])

# 후위 순회
def postorder(n):
    if n:
        preorder(left[n])
        preorder(right[n])
        print(n, end=" ")

V = int(input())
edge = list(map(int, input().split()))
E = V - 1   # V개의 정점이있는 트리의 간선 수

left = [0]*(V+1)     # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:            # p의 왼쪽 자식이 없으면
        left[p] = c
    else:                       # 왼쪽 자식이 없으면 오른쪽 자식으로 저장
        right[p] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()