import sys
sys.stdin = open("input.txt")

def VLR(s):
    queue.append(s)
    while queue:
        t = queue.pop(0)
        print(t, end=" ")
        for edge in edges[t]:
            VLR(edge)

v = int(input())
e = list(map(int, input().split()))

edges = [[] for _ in range(len(e))]

queue = []

for i in range((v-1)):
    edges[e[i*2]].append(e[i*2+1])

VLR(1)
