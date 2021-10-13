import sys
sys.stdin = open("input.txt")

def check(idx,idy): # Check Possible start and return
    for i in range(2):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            pass
        else:
            return False
    return True

def go(idx,idy,flag,flag_cnt,cnt): # idx, idy: now position, flag: direction, flag_cnt: memo for direction change, cnt: count for ans
    global stack, ans

    if cnt != 1 and flag_cnt == 4 and idx == start_idx and idy == start_idy: # no first, flag-direction 4, position == start position -> return
        ans = max(ans,cnt)
        return

    for i in range(2): # two direction: Go original direction, or change direction
        nr = idx + dirs[(flag+i)%4][0]
        nc = idy + dirs[(flag+i)%4][1]
        if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] not in stack:
            stack.append(maps[nr][nc])
            go(nr,nc,flag+i, flag_cnt+i, cnt+1) # recursion to next position
            stack.pop() # remove cookie what I already ate
        elif nr == start_idx and nc == start_idy: # for going to first-position
            go(nr,nc,flag+i, flag_cnt+i, cnt+1)



t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    dirs = [(1,1),(1,-1),(-1,-1),(-1,1)] # 0: right-down, 1: left-down, 2: left-up, 3: right-up
    ans = 1
    for i in range(n):
        for x in range(n):
            stack = [] # already ate species of cookie
            start_idx, start_idy = i, x
            stack.append(maps[i][x])
            if check(i,x):
                go(i,x,0,1,1) # idx, idy, flag(direction), flag-count, cnt for ans

    print("#" + str(tc), end=" ")
    print(ans-1) if ans != 1 else print(-1)

# Pass