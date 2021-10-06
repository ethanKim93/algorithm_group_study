import sys
sys.stdin = open('input.txt')


def preorder(mom):  # 전위 순회
    if tree.get(mom):
        print(mom, end=' ')
        preorder(tree[mom][0])
        if len(tree.get(mom)) == 2:
            preorder(tree[mom][1])
    else:
        print(mom, end=' ')

def inorder(mom):  # 중위 순회
    if tree.get(mom):
        inorder(tree[mom][0])
        print(mom, end=' ')
        if len(tree.get(mom)) == 2:
            inorder(tree[mom][1])
    else:
        print(mom, end=' ')


def postorder(mom):  # 후위순회
    if tree.get(mom):
        postorder(tree[mom][0])
        if len(tree.get(mom)) == 2:
            postorder(tree[mom][1])
        print(mom, end=' ')
    else:
        print(mom, end=' ')

N = int(input())
tree = {}
lst = list(input().split())
for i in range(N):
    if tree.get(lst[2 * i]):
        tree[lst[2 * i]] = tree[lst[2 * i]] + [lst[2 * i + 1]]
    else:
        tree[lst[2 * i]] = [lst[2 * i + 1]]
print(tree)
preorder('1')
print()
inorder('1')
print()
postorder('1')