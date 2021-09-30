import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    r, c = map(int,input().split())
    maps = [list(input()) for _ in range(r)]
    alist = []
    rules = {'211':0, '221':1, '122':2,'411':3, '132':4,'231':5, '114':6, '312':7, '213':8, '112':9}
    stack = []
    ans = 0
    for i in range(r-1,-1,-1):
        temps = ''
        for x in range(c-1,-1,-1):
            if maps[i][x] != '0':
                temps = maps[i][x] + temps
            if temps and maps[i][x] == '0' and temps not in alist:
                alist.append(temps)
        if temps and temps not in alist:
            alist.append(temps)

    for i in alist:
        x_to_int = int(i,16)
        int_to_b = '000' + bin(x_to_int)[2:]
        start = False
        f1 = f2 = f3 = 0
        temp = ""
        for x in range(len(int_to_b)-1,-1,-1):
            if int_to_b[x] == '1' and f2 == 0 and f3 == 0:
                f1 += 1
            elif int_to_b[x] == '0' and f1 != 0 and f3 == 0:
                f2 += 1
            elif int_to_b[x] == '1' and f2 != 0 and f1 != 0:
                f3 += 1
            elif f3 != 0 and int_to_b[x] == '0':
                mn = min(f1, f2, f3)
                print(f1,f2,f3)
                temp = str(rules[f'{f3 // mn}{f2 // mn}{f1 // mn}']) + temp
                f1 = f2 = f3 = 0
                if len(temp) == 8:
                    cnt = 0

                    for y in range(8):
                        if (y+1) % 2 == 0:
                            cnt += int(temp[y])
                        else:
                            cnt += int(temp[y])*3

                    if cnt % 10 == 0 and temp not in stack:
                        for z in range(8):
                            ans += int(temp[z])
                        stack.append(temp)




    print("#{} {}".format(tc,ans))