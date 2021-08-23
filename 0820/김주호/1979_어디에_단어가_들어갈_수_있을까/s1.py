T = int(input())

for case in range(T):
    N_K = input().split(" ")
    N = int(N_K[0])
    K = int(N_K[1])

    Array = [[0]] * N
    ans = [0] * N

    for i in range(N):
        line = input()
        if line[-1] == " ":
            line = line[:-1]
        Array[i] = list(map(int, line.split(" ")))
        cnt = 0
        for j in range(N):
            if Array[i][j]:
                cnt += 1
                if j == N - 1:
                    ans[cnt - 1] += 1
            elif cnt > 0:
                ans[cnt - 1] += 1
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if Array[i][j]:
                cnt += 1
                if i == N - 1:
                    ans[cnt - 1] += 1
            elif cnt > 0:
                ans[cnt - 1] += 1
                cnt = 0

    # print(True if [1] * K  == [1, 1, 1] else False)

    print(f"#{case + 1} {ans[K - 1]}")