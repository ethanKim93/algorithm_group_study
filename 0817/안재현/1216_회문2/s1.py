import sys

sys.stdin = open("input.txt")


def call_me(M, N):
        count = 0
        for j in range(N):
            for k in range(N-M+1):
                cnt = 0
                for t in range(M):
                    if empty_list[j][t+k] == empty_list[j][M+k-t-1]:
                        cnt += 1
                if cnt == M:
                    result = M
                    count += 1
                    return result
        if count == 0:
            for j in range(N):
                for k in range(N-M+1):
                    cnt = 0
                    for t in range(M):
                        if empty_list[t+k][j] == empty_list[M+k-t-1][j]:
                            cnt += 1
                    if cnt == M:
                        for i in range(M):
                            result = M
                            return result


T = 10
for tc in range(1, T+1):
    goal_list = []
    len = input()
    empty_list = []
    N = 100
    for i in range(N):
        N_list = list(map(str, input().split()))
        empty_list += N_list

    for M in range(100):
        try:
            if call_me(M, N) >= 0:
                result = call_me(M, N)
        except:
            continue
    print("#{} {}".format(tc, result), end=" ")
    print()