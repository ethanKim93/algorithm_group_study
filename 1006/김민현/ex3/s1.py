import sys
sys.stdin = open('input.txt')

def traversal(n):
    #print(n)#전위
    if nleft[n]:
        traversal(nleft[n])
    print(n)#중위
    if nright[n]:
        traversal(nright[n])
    #print(n)#후위

N = int(input())
nodes = list(map(int,input().split()))
nleft = [0]*(N+2)
nright = [0]*(N+2)

for i in range(0,len(nodes),2):
    if nleft[nodes[i]]:
        nright[nodes[i]] = nodes[i+1]
    else:
        nleft[nodes[i]] = nodes[i+1]

traversal(1)