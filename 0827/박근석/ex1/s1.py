import sys
sys.stdin = open('input.txt')

def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)



N = int(input())
line = list(map(int, input().split()))
E = N - 1
left = [0]*(N+1)
right = [0]*(N+1)
for i in range(E):
    p, c = line[i*2], line[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
        # 자식 노드의 순서가 없을 때
        # if left[p] > c:
        #     right[p] = left[p]
        #     left[p] = c
        # else:
        #     right[p] = c

pre_order(1)
in_order(1)
post_order(1)


