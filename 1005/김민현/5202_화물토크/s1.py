import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    dok = [list(map(int,input().split())) for _ in range(N)]
    queue = [0]
    visit = [0]*N
    cnt = 0
    start_idx = 0
    while queue:
        start_time = queue.pop(0)
        for i in range(N):
            if start_time < dok[i][0]:
                if not visit[i]:
                    visit[i] = cnt + 1
                    queue.append(dok[i][0])
        cnt += 1

    print('#{} {}'.format(tc,visit))