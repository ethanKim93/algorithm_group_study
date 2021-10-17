import sys
sys.stdin = open('s_input.txt')

def find_set(n):
    while p[n] != n:
        n = p[n]
    return n

# path compression 적용
def find_set2(n):
    if p[n] != n :
        p[n] = find_set2(p[n])
    return p[n]

T = int(input())
for tc in range(1,T+1):
    N, M =map(int,input().split())
    p = [i for i in range(N+1)]
    for k in range(M):
        s, e = map(int,input().split())
        p[find_set2(s)] = find_set2(e)
    res = set()
    for v in range(1,N+1):
        res.add(find_set2(v))
    print('#{} {}'.format(tc,len(res)))






# T = int(input())
# for tc in range(1,T+1):
#     N, M =map(int,input().split())
#     arr = [[] for _ in range(N+1)]
#     for i in range(M):
#         s,e = map(int,input().split())
#         arr[s].append(e)
#         arr[e].append(s)