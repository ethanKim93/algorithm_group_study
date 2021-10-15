import sys
sys.stdin = open('input.txt')

def find_set(n):
    while n != p[n]:
        n = p[n]
    return n
def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    friend = list(map(int,input().split()))
    p = list(range(N+1))
    for i in range(0,len(friend),2):
        union(friend[i],friend[i+1])
    team = []
    for i in range(N+1):
        team.append(find_set(i))
    print('#{} {}'.format(tc,len(set(team))))

