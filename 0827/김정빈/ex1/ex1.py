def preorder(T):
    if T:
        print(T, end=" ")
        preorder(left[T])
        preorder(right[T])

def inorder(T):
    if T:
        preorder(left[T])
        print(T, end=" ") #or visit(T)
        preorder(right[T])

def postorder(T):
    if T:
        preorder(left[T])
        preorder(right[T])
        print(T, end=" ")

"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
6
1 2 1 3 2 4 3 5 3 6
"""

V = int(input())
edge = list(map(int, input().split()))
E = V - 1   #V개의 정점이있는 트리의 간선 수

left = [0]*(V+1)     #부모를 인덱스로 자식번호 저장
right = [0]*(V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:            #p의 왼쪽 자식이 없으면
        left[p] = c
    else:                       #왼쪽 자식이 없으면 오른쪽 자식으로 저장
        right[p] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()