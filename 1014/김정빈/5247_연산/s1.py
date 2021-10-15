import sys
sys.stdin = open("input.txt")
#5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    tot = [0]*(2*M)

    def bfs():
        q = [N]
        while q:
            p = q.pop(0)
            if p == M:
                print('#{} {}'.format(tc, tot[p]))
                break
            for loc in (p+1, p-1, p*2, p-10):
                if 0<loc<=M*2 and not tot[loc]:
                    tot[loc] = tot[p]+1
                    q.append(loc)
    bfs()