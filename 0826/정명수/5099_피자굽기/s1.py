import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    q = [i for i in range(N)]
    k = N

    while q:
        for i in q:
            pizza[i] //= 2
        for i in range(N):
            if q:
                if pizza[q[0]] != 0:
                    q.append(q.pop(0))
                else:
                    answer = q.pop(0)
                    if k < M:
                        q.insert(0,k)
                        k += 1
        if pizza == [0]*M:
            break
    print('#{} '.format(tc), end = '')
    print(answer+1)

