#5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(left[n])
        preorder(right[n])

T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    pc = list(map(int, input().split()))
    left = [0 for _ in range(e + 2)]
    right = [0 for _ in range(e + 2)]
    for i in range(0, len(pc), 2):
        p, c = pc[i], pc[i+1]
        if left[p]:
            right[p] = c
        else:
            left[p] = c
    cnt = 0
    preorder(n)
    print('#{} {}'.format(tc, cnt))