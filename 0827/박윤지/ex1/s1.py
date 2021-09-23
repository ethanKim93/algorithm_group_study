import sys
sys.stdin = open('input.txt')


# 전위순회
def preorder(v):
    if v:
        print(v)
        preorder(left[v])
        preorder(right[v])


# 중위순회
def inorder(v):
    if v:
        inorder(left[v])
        print(v)
        inorder(right[v])


# 후위순회
def postorder(v):
    if v:
        postorder(left[v])
        postorder(right[v])
        print(v)


T = 1

for tc in range(1, T+1):
    V = int(input())
    edge = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)
    for i in range(V-1):
        if left[edge[i*2]] == 0:
            left[edge[i*2]] = edge[i*2+1]
        else:
            right[edge[i * 2]] = edge[i * 2 + 1]
    preorder(1)
    # inorder(1)
    # postorder(1)