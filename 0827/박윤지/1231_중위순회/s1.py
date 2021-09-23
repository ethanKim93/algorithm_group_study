import sys
sys.stdin = open('input.txt')


def inorder(n):
    global result
    if n:
        inorder(left[n])
        result += alphabet[n]
        inorder(right[n])


T = 10

for tc in range(1, T+1):
    N = int(input())
    alphabet = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = ''
    for i in range(N):
        link = list(input().split())
        alphabet[int(link[0])] = link[1]
        if len(link) == 3:
            left[int(link[0])] = int(link[2])
        elif len(link) == 4:
            left[int(link[0])] = int(link[2])
            right[int(link[0])] = int(link[3])
    inorder(1)
    print('#{} {}'.format(tc, result))