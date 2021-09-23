import sys
sys.stdin = open("input.txt")

def in_order(v):
    if v:
        in_order(left[v])
        print(P[v], end="")
        in_order(right[v])

for tc in range(1, 11):
    N = int(input())
    P = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for _ in range(N):
        p, alpha, *C = input().split()
        p = int(p)
        P[p] = alpha
        if C:
            for c in map(int, C):
                if not left[p]:
                    left[p] = c
                else:
                    right[p] = c
    print('#{}'.format(tc), end=" ")
    in_order(1)
    print()

