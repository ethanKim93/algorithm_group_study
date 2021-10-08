import sys
sys.stdin = open('input.txt')

def backtrack(k, p):
    global max_prob
    if p <= max_prob: return
    if k == N:
        max_prob = max(p, max_prob)
    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                backtrack(k+1, p*prob[k][w]/100)
                visited[w] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    max_prob = 0
    backtrack(0, 1)
    print('#{} {:.6f}'.format(tc, round(max_prob*100, 6)))