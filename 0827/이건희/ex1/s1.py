import sys

sys.stdin = open("input.txt")


def preorder_traverse(n): # p > l > r
    if n:
        print(n, end=" ")
        preorder_traverse(left[n])
        preorder_traverse(right[n])
    return

def inorder_traverse(n): # l > p > r
    if n:
        inorder_traverse(left[n])
        print(n, end=" ")
        inorder_traverse(right[n])

def postorder_traverse(n): # l > r > p
    if n:
        postorder_traverse(left[n])
        postorder_traverse(right[n])
        print(n, end=" ")

node = int(input())
edge = list(map(int, input().split()))
edge_num = node - 1
left = [0] * (node + 1) # 1/2 left
right = [0] * (node + 1) # 1/2 right
for i in range(edge_num):
    p, c = edge[2 * i], edge[2 * i + 1]

    if left[p] == 0:
        left[p] = c

    else:
        right[p] = c

preorder_traverse(1) # 전위 순회
print()
inorder_traverse(1) # 중위 순회
print()
postorder_traverse(1) # 후위 순회
