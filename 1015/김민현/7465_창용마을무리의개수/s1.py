import sys
sys.stdin = open('s_input.txt')

T = int(input())

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x,y):
    parent[find_set(y)] = find_set(x)

for tc in range(1,T+1):
    N,M = map(int,input().split())
    parent = [i for i in range(N+1)]

    for i in range(M):
        start,end = map(int,input().split())
        union(start,end)

    result = []
    for i in range(len(parent)):
        result.append(find_set(i))
    print('#{} {}'.format(tc,len(set(result))-1))

