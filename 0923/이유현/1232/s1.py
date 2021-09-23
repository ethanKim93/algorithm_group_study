import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)

    for _ in range(N):
        temp = list(input().split())
        if len(temp) > 2:
            tree[int(temp[0])] = temp[1]
        else:
            tree[int(temp[0])] = int(temp[1])

    