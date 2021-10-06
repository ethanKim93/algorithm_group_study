import sys
sys.stdin = open('sample_input.txt')

def backtrack(r, c):
    global ans, tot
    if tot > ans:
        return

    if r == N - 1 and c == N - 1:
        if tot < ans:
            ans = tot
            return
    for d in range(2):
        if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N:
            tot += matrix[r + dr[d]][c + dc[d]]
            backtrack(r + dr[d], c + dc[d])
            tot -= matrix[r + dr[d]][c + dc[d]]
    
    

T = int(input())
tot = 0
dr = [0, 1]
dc = [1, 0]
for tc in range(1, T+1):
    N = int(input())
    matrix = [[] for _ in range(N)]
    ans = 10000
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
    tot = matrix[0][0]
    backtrack(0, 0)
    print('#{} {}'.format(tc, ans))