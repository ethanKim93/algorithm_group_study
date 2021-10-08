# 정빈님 코드
def dfs(n, tot):
    global res
    if tot > res:  # 가지치기
        return
    if n == N:  # 다 순회했는지 확인
        if tot < res:
            res = tot
        return
    for i in range(N):  # 0~N-1
        if seled[i] == 0:
            seled[i] = 1
            dfs(n+1, tot+value[n][i])
            seled[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    value = [list(map(int,input().split())) for _ in range(N)]
    seled = [0]*N  # 방문 확인
    res = 9999  # 최대값으로 설정 == min value
    dfs(0, 0)
    print('#{} {}'.format(tc, res))