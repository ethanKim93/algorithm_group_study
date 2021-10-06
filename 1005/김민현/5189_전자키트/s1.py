import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]

    visit = [0]*N
    start,end = 0,0
    queue = []
    queue.append(start)
    while queue:
        start= queue.pop(0)
        for i in range(1,N):
            if not visit[i]:
                visit[i] = visit[start]+ office[start][i]
                queue.append(i)

    print(visit)
