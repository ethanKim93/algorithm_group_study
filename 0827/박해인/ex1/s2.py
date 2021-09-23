#중위순회
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])

V = int(input())
edges = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    p, c = edges[2*i], edges[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

in_order(1)
'''
12 7 4 2 1 8 5 9 3 10 6 13 11 
'''