import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    route = []
    for _ in range(N):
        AB = list(map(int, input().split()))
        route.extend(AB)

    # 정류장 번호 리스트로 받기
    P = int(input())
    stop = []
    for _ in range(P):
        stop.append(int(input()))

    result = []
    for bs in stop:
        cnt = 0
        for a in range(0, len(route), 2):
            if route[a] <= bs <= route[a+1]:
                cnt += 1
        result.append(cnt)

    print('#{}'.format(tc), end=' ')
    print(*result)
