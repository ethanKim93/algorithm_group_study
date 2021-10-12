def get_percent(status, turn):
    if turn == N:
        return 1

    if dp[status] != 0:
        return dp[status]
        
    for i in range(N):
        if not status & (1 << i):
            dp[status] = max(dp[status], get_percent(status | 1 << i, turn + 1) * works[turn][i])
    return dp[status]

for tc in range(1, int(input()) + 1):
    N = int(input())
    works = [list(map(lambda x : int(x) / 100, input().split())) for _ in range(N)]
    dp = [0] * (2 << N)
    print("#{} {}".format(tc, format(get_percent(0, 0) * 100, ".6f")))