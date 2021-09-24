import sys
sys.stdin = open("input.txt")
#5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
def heap(i):
    while tree[i//2] and tree[i//2] > tree[i]:
        tree[i//2], tree[i] = tree[i], tree[i//2]
        i //= 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ns = list(map(int, input().split()))
    tree = [0]+Ns
    tot = 0

    for i in range(2,N+1):
        heap(i)
    while N > 0:
        N //= 2
        tot += tree[N]
    print('#{} {}'.format(tc, tot))

"""
#1 7
#2 5
#3 65
"""