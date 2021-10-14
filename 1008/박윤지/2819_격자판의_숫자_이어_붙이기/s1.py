# 격자판을 이동하며 만들 수 있는 서로 다른 일곱 자리 수들의 개수

# 지나왔던 자리를 가도 되므로 visited 처리가 필요 없다
# 격자판의 모든 위치에서 dfs를 해야한다

import sys
sys.stdin = open('sample_input.txt', 'r')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, number, cnt):  # r, c: 현재 위치 / number: 지금까지 만든 숫자 / cnt: 지금까지 선택한 숫자수
    global ans
    if cnt >= 7:
        ans.add(number)
        return

    ir = r
    ic = c
    for i in range(4):
        nr = ir + dr[i]
        nc = ic + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, number + arr[nr][nc], cnt+1)


T = int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '', 0)
    print('#{} {}'.format(tc, len(ans)))

