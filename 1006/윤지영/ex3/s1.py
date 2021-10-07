import sys
sys.stdin = open('input.txt')

# 전위순회
def preorder(n):
    if n :
        preo.append(n)
        preorder(tree[n][0])
        preorder(tree[n][1])

# 중위순회
def inorder(n):
    if n :
        inorder(tree[n][0])
        ino.append(n)
        inorder(tree[n][1])

# 후위순회
def postorder(n):
    if n :
        postorder(tree[n][0])
        postorder(tree[n][1])
        posto.append(n)


V = int(input())
li = list(map(int,input().split()))
tree = [[0,0] for _ in range(V+2)]
for i in range(0,2*V-1,2):
    if tree[li[i]][0]:
        tree[li[i]][1] = li[i+1]
    else:
        tree[li[i]][0] = li[i+1]

ino = []
preo = []
posto = []
postorder(1)
inorder(1)
preorder(1)
print(ino, preo,posto)

