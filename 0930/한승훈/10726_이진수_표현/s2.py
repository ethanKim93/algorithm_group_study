for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    flag = "ON"
    for idx in range(N):
        if M & (1 << idx):
            continue
        flag = "OFF"
    print("#{} {}".format(tc, flag))

    # M = 1000001000
    #     0000001000 idx가 3일때
    #     0000000100 idx가 2일때
    #     0000000010 idx가 1일때
    #     0000000001 idx가 0일때
