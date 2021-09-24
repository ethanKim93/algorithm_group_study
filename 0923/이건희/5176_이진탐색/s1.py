import sys
sys.stdin = open("input.txt")

t = int(input())

def inorder(root):
    global cnt, values
    if root:
        inorder(temps1[root])
        values[root] = cnt
        cnt += 1
        inorder(temps2[root])

    return


for tc in range(1, t + 1):
    n = int(input())
    temps1 = [0] * (n + 1)
    temps2 = [0] * (n + 1)
    values = [0] * (n + 1)
    cnt = 1
    for i in range(1, n + 1):
        if 2 * i <= n:
            temps1[i] = 2 * i
        if 2 * i + 1 <= n:
            temps2[i] = 2 * i + 1

    inorder(1)
    print("#{} {} {}".format(tc, values[1], values[n // 2]))
