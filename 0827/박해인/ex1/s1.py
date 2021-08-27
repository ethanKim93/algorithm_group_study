#전위순회
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])


V = int(input())
edges = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    p, c = edges[i*2], edges[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

pre_order(1)
'''
1 2 4 7 12 3 5 8 9 6 10 11 13 
'''