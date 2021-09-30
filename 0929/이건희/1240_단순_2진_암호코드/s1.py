import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    n, m = map(int,input().split())
    maps = [list(input()) for _ in range(n)]
    rules = {'0111011': 7, '0110001': 5, '0001101': 0, '0010011': 2, '0011001':1, '0111101':3, '0100011':4, '0101111':6, '0110111':8, '0001011':9}
    for i in range(n):
        for x in range(m):
            if maps[i][x] == '1':
                start_r = i
                start_c = x


    subans = ""
    temps = ""
    cnt = 0
    for x in range(start_c,-1,-1):
        temps = maps[start_r][x] + temps
        cnt += 1
        if cnt == 7 and len(subans) < 56:
            cnt = 0
            subans = temps + subans
            temps = ""

    ans = []
    for i in range(0,len(subans),7):
        ans.append(rules[subans[i:i+7]])

    result = 0
    anscnt = 0
    for i in range(8):
        if (i+1) % 2 == 0:
            result += ans[i]
        else:
            result += ans[i]*3
        anscnt += ans[i]
    if result % 10 == 0:
        print("#{} {}".format(tc,anscnt))
    else:
        print("#{} {}".format(tc,0))

# Pass