import sys
sys.stdin = open("input.py")

def patrol(x):
    if x:
        print(x)
        patrol(left[x])
        patrol(right[x])


node = int(input())
edge = list(map(int,input().split()))
left = [0]*(node+1)
right = [0]*(node+1)
for i in range(node-1):
    s,g = edge[i*2],edge[i*2+1]
    if left[s] == 0:
        left[s] = g
    else:
        right[s] = g

patrol(1)
#print(edge)
#print('#{} {}'.format(tc,ans))