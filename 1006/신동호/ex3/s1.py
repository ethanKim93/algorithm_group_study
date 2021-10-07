# 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 8
# 1 2 1 3 2 4 2 5 3 6 3 7 5 8 5 9

N = int(input())
A = list(map(int, input().split()))

def preorder(s):
    global L, R
    if s:
        print(s, end=' ')
        preorder(L[s])
        preorder(R[s])

def inorder(s):
    global L, R
    if s:
        inorder(L[s])
        print(s, end=' ')
        inorder(R[s])

def postorder(s):
    global L, R
    if s:
        postorder(L[s])
        postorder(R[s])
        print(s, end=' ')

L = [0] * (N+2)
R = [0] * (N+2)

for i in range(0, len(A), 2):
    if not L[A[i]]:
        L[A[i]] = A[i+1]
    else:
        R[A[i]] = A[i+1]

print(L, R)
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()