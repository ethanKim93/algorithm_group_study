def make(N):
    for i in range(N):
        parents[i] = i

def find(el):
    if el == parents[el]:
        return el
    parents[el] = find(parents[el])
    return parents[el]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot:
        return False

    parents[bRoot] = aRoot

    return True

N = 5 # 원소 개수
parents = [0] * N

make(N)
print(parents)
union(0, 1)
print(parents)
union(2, 1)
print(parents)
union(3, 2)
print(parents)
union(4, 3)
print(parents)
print('===========================')
find(4)
print(parents)
find(3)
print(parents)
find(2)
print(parents)
find(1)
print(parents)
