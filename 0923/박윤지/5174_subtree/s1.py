import sys
sys.stdin = open('sample_input.txt')

def preorder(n):
    global cnt
    if n:  # 0이 아닐 때
        cnt += 1
        preorder(left[n])
        preorder(right[n])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    left = [0] * (E+2)  # 왼쪽, 오른쪽의 구별이 필요 없지만 그냥 썼다.
    right = [0] * (E+2)
    for i in range(0, E*2-1, 2):
        if left[edge[i]] != 0:
            right[edge[i]] = edge[i+1]
        else:
            left[edge[i]] = edge[i+1]
    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc, cnt))

