import sys
sys.stdin = open("input.txt")

def preorder(start):
    if not start:
        return

    print(start, end=" ")
    preorder(left[start])
    preorder(right[start])

def inorder(start):
    if not start:
        return

    inorder(left[start])
    print(start, end=" ")
    inorder(right[start])

def postorder(start):
    if not start:
        return

    postorder(left[start])
    postorder(right[start])
    print(start, end=" ")


v = int(input())
maps = list(map(int,input().split()))

left = [0]*(v+1)
right = [0]*(v+1)

for i in range(0,len(maps),2):
    if not left[maps[i]]:
        left[maps[i]] = maps[i+1]
    else:
        right[maps[i]] = maps[i+1]

preorder(1)
print()
inorder(1)
print()
postorder(1)

# Pass