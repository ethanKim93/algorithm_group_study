import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    maps = [list(input()) for i in range(n)]
    r_list = []
    c_list = []
    ans = 0
    for i in range(n):
        r_word = ""
        for x in range(n-m+1):
            r_word = maps[i][x:x+m]
            c_word = []

            for y in range(m):
                c_word.append(maps[x+y][i])
            c_list.append(c_word)
        r_list.append(r_word)

    for i in r_list:
        if i == i[::-1]:
            ans = i

    for i in c_list:
        if i == i[::-1]:
            ans = i

    print("#{} {}".format(tc, "".join(map(str,ans))))