import sys
sys.stdin = open('input.txt')

def inorder(idx):
    if idx > N:
        return
    # left
    if (idx * 2) <= N:
        inorder(idx * 2)
    result.append(node[idx])
    # right
    if (idx * 2 + 1) <= N:
        inorder(idx * 2 + 1)

for tc in range(10):
    N = int(input())
    node = [0] * (N+1)
    for n in range(N):
        vals = list(input().split())
        node[int(vals[0])] = vals[1]
    result = []
    inorder(1)
    print("#{} {}".format(tc +1, ''.join(result)))