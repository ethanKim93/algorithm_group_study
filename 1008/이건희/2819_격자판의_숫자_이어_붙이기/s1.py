import sys
sys.stdin = open("input.txt")

def check(idx, idy, now):
    if len(now) == 7:
        if now not in subans:
            subans.append(now)
        return

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            check(nr, nc, now+maps[nr][nc])

t = int(input())
for tc in range(1, t+1):
    maps = [list(map(str,input().split())) for _ in range(4)]
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    subans = []
    for i in range(4):
        for x in range(4):
            check(i, x, str(maps[i][x]))

    print("#{} {}".format(tc,len(subans)))

# Pass