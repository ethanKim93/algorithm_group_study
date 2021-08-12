import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    mx = 0 # 최댓값

    for i in range(n):
        for x in range(n): # map 중심 좌표 = maps[i][x]
            sm = 0 # 한번 내려치고 초기화
            for y in range(m): # 파리채 범위 = maps[i+y][x+z]
                for z in range(m):
                    nr = i + y
                    nc = x + z
                    if 0 <= nr < n and 0 <= nc < n:
                        sm += maps[nr][nc]
            if sm > mx: #=max(sm,mx)
                mx = sm


    print("#{} {}".format(tc, mx))