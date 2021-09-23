import sys
sys.stdin = open("input.txt")

def inorder(T):
    if T:
        inorder(left[T])
        print(T, end=" ") #or visit(T)
        inorder(right[T])

for tc in range(1, 11):
    N = int(input())

    p = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(1, N+1):
        c = list(input().split())
        p[int(c[0])] = c[1]
        if len(c[2:]) == 2:
            left[int(c[0])] = int(c[2])
            right[int(c[0])] = int(c[3])
        elif len(c[2:]) == 1:
            left[int(c[0])] = int(c[2])

    inorder(1)
    print()
