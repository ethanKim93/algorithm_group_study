
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])
def inorder(n):
    if n:
        preorder(left[n])
        print(n, end=" ") #or visit(T)
        preorder(right[n])
def postorder(n):
    if n:
        preorder(left[n])
        preorder(right[n])
        print(n, end=" ")



V = int(input())
edges = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    p, c = edges[i*2], edges[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()

