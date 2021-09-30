alist = list(input())
temps = ''
cnt = 0
for i in range(len(alist)):
    temps += alist[i]
    cnt += 1
    if cnt == 7:
        if i != len(alist)-1:
            print(int(temps, 2), end=", ")
        else:
            print(int(temps,2))
        temps = ''
        cnt = 0