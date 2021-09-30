
t = int(input())
for tc in range(1,t+1):
    r, c = map(int,input().split())
    maps = [list(input()) for _ in range(r)]
    alist = []
    rules = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
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
        for x in range(len(int_to_b),55,-1):
            check = int_to_b[x-56:x]
            if check[-1] == '0':
                continue
            else:
                temps = []
                for y in range(0,56,7):
                    if check[y:y+7] in rules:
                        temps.append(rules.index(check[y:y+7]))
                    else:
                        break

                if len(temps) == 8 and temps not in stack:
                    stack.append(temps)
                    subans = 0
                    for z in range(8):
                        if (z+1) % 2 == 1:
                            subans += temps[z] * 3
                        else:
                            subans += temps[z]

                    if subans % 10 == 0:
                        for a in temps:
                            ans += int(a)

    print("#{} {}".format(tc,ans))

# Fail: Wrong Anser