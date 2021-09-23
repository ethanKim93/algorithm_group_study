for case in range(int(input())):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))

    result = "Possible"

    cnt = 0
    for i in range(N):
        if people[i] // M * K - cnt < 1:
            result = "Impossible"
            break
        cnt += 1

    print("#{} {}".format(case + 1, result))
