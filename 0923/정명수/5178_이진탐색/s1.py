import sys
sys.stdin = open("input.txt")

def tree(n):
    global cnt
    if n <= N:
        tree(2*n)
        cnt += 1
        tree_idx[n] = cnt
        tree(2*n+1)
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree_idx = [0]*(N+1)
    cnt = 0
    tree(1)
    print('#{} {} {}'.format(tc,tree_idx[1],tree_idx[N//2]))

