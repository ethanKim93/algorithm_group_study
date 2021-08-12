import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    ans = 0

    # Row_search
    for i in range(n):
        cnt = 0
        for x in range(n):
            if maps[i][x] == 0:
                cnt = 0
            else:
                cnt += maps[i][x]

            if cnt == k:
                if x+1 == n:
                    ans += 1
                elif maps[i][x+1] == 0:
                    ans += 1

    # Col_search
    for x in range(n):
        cnt = 0
        for i in range(n):
            if maps[i][x] == 0:
                cnt = 0
            else:
                cnt += maps[i][x]

            if cnt == k:
                if i+1 == n:
                    ans += 1
                elif maps[i+1][x] == 0:
                    ans += 1

    print("#{} {}".format(tc,ans))