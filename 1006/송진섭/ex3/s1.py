"""
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def preorder(node):                              # 중위순회
    if tree[node]:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])


def inorder(node):                              # 중위순회
    if tree[node]:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])


def postorder(node):                              # 중위순회
    if tree[node]:
        postorder(left[node])
        print(node, end=' ')
        postorder(right[node])


N = int(input())
line = list(map(int, input().split()))
left = [0] * (N+2)
right = [0] * (N+2)
tree = [0] + [1] * (N+1)
for i in range(N):
    if not left[line[2*i]]:
        left[line[2*i]] = line[2*i+1]

    else:
        right[line[2 * i]] = line[2 * i + 1]

print('전위')
preorder(1)
print()
print('중위', end='\n')
inorder(1)
print()
print('후위', end='\n')
postorder(1)




