import sys
sys.stdin = open('input.txt')

def check(row, newone):
    global ans
    if newone <= ans:
        return
    if row == N:
        ans = newone
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                check(row+1, newone*pi[i][row]/100)
                visited[i] = 0
for tc in range(1, int(input())+1):
    ans = 0
    N = int(input())
    visited = [0]*N
    pi = [list(map(int, input().split())) for _ in range(N)]
    check(0, 1)
    ans *= 100
    ans = format(ans, '.6f')
    print('#{} {}'.format(tc, ans))
