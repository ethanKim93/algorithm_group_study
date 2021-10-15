import sys
sys.studin = open('sample_input.txt','r')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x,y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = list(map(int,input().split()))
    parent = [i for i in range(N + 1)]
    for i in range(0,len(L),2):
        union(L[i],L[i+1])
    result = set()
    for i in range(1, N + 1):
        result.add(find_set(i))

    print("#{} {}".format(tc, len(result)))