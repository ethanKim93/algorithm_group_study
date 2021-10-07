import sys
sys.stdin = open('input.txt')

N = int(input())
edge = list(map(int,input().split()))
left=[0]*15
right = [0]*15
for i in range(0,len(edge),2):
    if left[edge[i]]:
        right[edge[i]] = edge[i+1]
    else:
        left[edge[i]] = edge[i+1]

def ftree(n):
    if n:
        print(n, end=' ')
        ftree(left[n])
        ftree(right[n])
def mtree(n):
    if n:
        mtree(left[n])
        print(n, end=' ')
        mtree(right[n])
def btree(n):
    if n:
        btree(left[n])
        btree(right[n])
        print(n, end=' ')

ftree(1)
print()
mtree(1)
print()
btree(1)
