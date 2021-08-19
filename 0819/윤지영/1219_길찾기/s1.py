import sys
sys.stdin = open("input.txt")

T = 10

# 스택 이용
for _ in range(1,T+1):
    A, B = 0, 99
    G = [[0] * 100 for _ in range(100)]
    visited = [0] * 100
    stack = []
    result = []
    tc, N = map(int, input().split())
    li = input().split()
    for i in range(0,N*2,2):              # 2칸씩 건너뛰니까 끝값이 N * 2 해야함
        u,v = int(li[i]), int(li[i+1])
        G[u][v] = 1
    visited[A] = 1
    stack.append(A)
    while True:
        for w in range(100):
            if G[A][w] == 1 and not visited[w]:
                stack.append(w)
                visited[w] = 1
                A = w
                result.append(A)
                break
        else:
            if stack:
                A = stack.pop()
            else:
                break
    if B in result:
        cnt = 1
    else:
        cnt = 0
    print('#{} {}'.format(tc,cnt))

# 재귀 이용


def dfs(s):
    visited[s] = 1
    for w in range(100):
        if G[s][w] == 1 and visited[w] == 0:
            dfs(w)


for _ in range(1,T+1):
    A, B = 0, 99
    G = [[0] * 100 for _ in range(100)]
    visited = [0] * 100
    tc, N = map(int, input().split())
    li = input().split()
    for i in range(0,N*2,2):             # 2칸씩 건너뛰니까 끝값이 N * 2 해야함
        u,v = int(li[i]), int(li[i+1])
        G[u][v] = 1
    dfs(A)

    print('#{} {}'.format(tc,visited[99]))