import sys
sys.stdin = open("input.txt")

def check(idx,idy):
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            if maps[nr][nc] == maps[idx][idy]+1:
                return True
    return False

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    temps = [0]*(n**2+1)

    for i in range(n):
        for x in range(n):
            if check(i,x):
                temps[maps[i][x]] = 1

    ans = 0
    ans_idx = 987654321
    cnt = flag = 0
    start = 0
    for i in range(len(temps)):
        if temps[i] and not flag:
            cnt += 1
            start = i
            flag=1

        elif temps[i]:
            cnt += 1

        else:
            if cnt > ans:
                ans = cnt
                ans_idx = start

            cnt = 1
            flag = 0

    print("#{} {} {}".format(tc, ans_idx, ans))

# Pass