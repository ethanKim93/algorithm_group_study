for case in range(int(input())):
    Start = []
    End = []
    N = int(input())

    for _ in range(N):
        S, E = map(int, input().split())
        Start.append(S)
        End.append(E)

    P = int(input())
    li = [0] * P

    for c in range(P):
        num = int(input())
        cnt = 0

        for i in range(N):
            if Start[i] <= num <= End[i]:
                cnt += 1

        li[c] = cnt

    print("#{}".format(case + 1), end=" ")
    print(*li)