#6485. 삼성시의 버스 노선
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    stop = [0]*5000
    for _ in range(N):
        ai, bi = map(int,input().split())
        for check in range(ai-1, bi):
            stop[check] += 1

    P = int(input())
    C = [int(input()) for _ in range(P)]
    ans = []
    for c in C:
        ans.append(stop[c-1])

    print('#{} {}'.format(tc, " ".join(map(str,ans))))