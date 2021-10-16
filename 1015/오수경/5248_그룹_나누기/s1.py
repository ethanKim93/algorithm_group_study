import sys
sys.stdin = open('sample_input.txt')

def Find_Set(x):
    if ppl[x] == x:
        return x
    else:
        return Find_Set(ppl[x])

def Union(x, y):
    ppl[Find_Set(y)] = Find_Set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    vote = list(map(int, input().split()))
    ppl = list(range(N+1))
    for i in range(M):
        x, y = vote[2*i], vote[2*i+1]
        Union(x, y)

    for i in range(1, N+1):
        ppl[i] = Find_Set(i)
    cnt = set(ppl[1:])
    print('#{} {}'.format(tc, len(cnt)))