import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = [[] for _ in range(N)]
    for i in range(N):
        time[i] = list(map(int, input().split()))
    time.sort(key=lambda x:-x[1])
    end = -1
    ans = 0
    while time:
        s, e = time.pop()
        if s >= end:
            ans += 1
            end = e
    print('#{} {}'.format(tc, ans))

        