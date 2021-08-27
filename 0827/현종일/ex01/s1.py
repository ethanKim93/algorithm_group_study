import sys
sys.stdin = open("input.txt")

def VLR(s):
    print(s, end=" ")
    for edge in edges[s]:
        VLR(edge)

v = int(input())
e = list(map(int, input().split()))

edges = [[] for _ in range(len(e))]

for i in range((v-1)):
    edges[e[i*2]].append(e[i*2+1])

VLR(1)
