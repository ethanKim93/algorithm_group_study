import sys
sys.stdin = open('sample_input.txt')

def backtrack(v):
    global visited, check, tot, ans
    if check == N-1:
        tot += matrix[v][1]
        # print(v, 1, tot)
        if tot < ans:
            ans = tot
        tot -= matrix[v][1]
        return
    for i in range(2, N+1):
        if not visited[i]:
            visited[i] = 1
            check += 1
            tot += matrix[v][i]
            # print(v, i, matrix[v][i], tot)
            backtrack(i)
            visited[i] = 0
            check -= 1
            tot -= matrix[v][i]
    


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    tot = 0
    ans = 10000000
    check = 0
    for i in range(1, N+1):
        matrix[i] = [0] + list(map(int, input().split()))
    backtrack(1)
    print('#{} {}'.format(tc, ans))
