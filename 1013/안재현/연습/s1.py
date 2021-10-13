import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
edge = list(map(int, input().split()))

adjM = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*1], edge[2*i+1]
    adjM[n1][n2] = 1
    # adjM[n2][n1] = 1
print(adjM)
print()
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*1], edge[2*1+1]
    adjL[n1].append(n2)
    # adjL[n2].append(n1)
print(adjL)
