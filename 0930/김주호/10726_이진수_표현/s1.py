for case in range(int(input())):
    N, M = map(int, input().split())

    flag = True
    for i in range(N):
        if not (M >> i & 1):
            flag = False
            break

    print("#{} {}".format(case + 1, "ON" if flag else "OFF"))
