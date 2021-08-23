for case in range(int(input())):
    li = []
    for _ in range(int(input())):
        Now, Goto = map(int, input().split())
        if Now > Goto:
            li.append([Goto, Now])
        else:
            li.append([Now, Goto])

    li.sort(key=lambda x: (x[0], x[1]))

    t = 1
    i = 0
    start = 0
    while len(li):
        if i < len(li):
            if start < li[i][0]:
                start = li[i][1] + 1 if li[i][1] % 2 else li[i][1]  # 1 > 3, 4 > 6이 왜 겹쳐 ㅂㄷㅂㄷ
                del (li[i])
            else:
                i += 1
        else:
            t += 1
            i = 0
            start = 0

    print("#{} {}".format(case + 1, t))
