'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def VLR(n): # 전위순회
    if n:
        print(n, end = ' ')
        VLR(LEFT[n])
        VLR(RIGHT[n])

def LVR(n): # 중위순회
    if n:
        VLR(LEFT[n])
        print(n, end = ' ')
        VLR(RIGHT[n])

def LRV(n): # 후위순회
    if n:
        VLR(LEFT[n])
        VLR(RIGHT[n])
        print(n, end = ' ')

V = int(input())
E = V - 1
edges = list(map(int, input().split()))

LEFT = [0] * (V+1)
RIGHT = [0] * (V+1)

for i in range(E):
    if not LEFT[edges[2 * i]]:
        LEFT[edges[2 * i]] = edges[2 * i + 1]
    else:
        RIGHT[edges[2 * i]] = edges[2 * i + 1]

VLR(1)
print('VLR 전위순회')
print()
LVR(1)
print('LVR 중위순회')
print()
LRV(1)
print('LRV 후위순회')
print()