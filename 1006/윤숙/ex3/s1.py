import sys

sys.stdin = open('input.txt')


def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])


def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end=' ')


link_num = int(input())
arr = list(map(int, input().split()))
checked = [0] * (link_num + 2)
left = [0] * (link_num + 2)
right = [0] * (link_num + 2)
# n개의 정점일 때, n-1개의 간선
for i in range(0, link_num * 2, 2):
    P, C = arr[i], arr[i + 1]
    if left[P]:
        right[P] = C
    else:
        left[P] = C
print('전위 순회')
pre_order(1)
print()
print('중위 순회')
in_order(1)
print()
print('후위 순회')
post_order(1)