for case in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))

    total = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            num = li[i] * li[j]
            st = str(num)
            for k in range(len(st) - 1):
                if int(st[k]) > int(st[k + 1]):
                    break
            else:
                if total < num:
                    total = num

    print("#{} {}".format(case + 1, total))