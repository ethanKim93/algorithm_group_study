import sys

sys.stdin = open("input.txt")

def inorder_traval(pos):
    if maps[pos]:
        inorder_traval(int(left[pos]))
        print(maps[pos], end="")
        inorder_traval(int(right[pos]))

for tc in range(1, 11):
    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n+1)
    maps = [0] * (n+1)
    for i in range(n):
        key = list(input().split())
        for idx, x in enumerate(key):
            if idx == 0:
                k = int(x)
            elif idx == 1:
                maps[k] = x
            elif idx == 2:
                left[k] = x
            else:
                right[k] = x

    print("#" + str(tc), end=" ")
    inorder_traval(1)
    print()