#5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
def inorder(n):
    global k
    if n <= N:
        inorder(n*2)
        tree[n-1] = k
        k += 1
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*N
    k = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[0], tree[N//2-1]))