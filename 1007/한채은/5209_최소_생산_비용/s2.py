import sys
sys.stdin = open('sample_input.txt')

def cost(idx, total):
    global result

    if total >= result:
        return

    if idx == N:
        result = total
        return

    # N만큼 돌면서
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cost(idx+1, total + arr[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 99999
    cost(0,0)
    print('#{} {}'.format(tc, result))