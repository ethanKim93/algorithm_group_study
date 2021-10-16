import sys
sys.stdin = open('sample_input.txt')

def bfs(n):
    global ans
    q = [n]
    while q:
        x = q.pop(0)
        if x == M:
            ans = check[x]
            break
        else:
            for nx in (x+1, x-1, 2*x, x-10):
                if 0 < nx <= M*2+1 and not check[nx]:
                    check[nx] = check[x] + 1
                    q.append(nx)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 10000
    check = [0]* (M*2)+1
    bfs(N)
    print('#{} {}'.format(tc, ans))