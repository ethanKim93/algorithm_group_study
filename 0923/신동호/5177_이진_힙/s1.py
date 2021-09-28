import sys
sys.stdin = open('sample_input.txt')

def order(t):
    while t<=N:
        if not tree[t]:
            t2 = t
            tree[t2] = numbers[t2-1]
            while not tree[t2//2] <= tree[t2]:
                tree[t2//2], tree[t2] = tree[t2], tree[t2//2]
                t2 //= 2
        t += 1

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N+1)
    tot = 0
    order(1)
    while N:
        N //= 2
        tot += tree[N]
    print('#{} {}'.format(tc, tot))
