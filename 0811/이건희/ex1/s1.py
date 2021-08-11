import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    dirs = [(-1,0), (1,0), (0,-1), (0,1)] # Dir
    res = 0

    for r in range(n):
        for c in range(n):
            for d in range(4):
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]

                if 0 <= nr < n and 0 <= nc < n: # Check move possible
                    one = maps[nr][nc] - maps[r][c]
                    if one < 0:
                        one = -one # =abs(one)
                    res += one

    print("#{} {}".format(tc, res))