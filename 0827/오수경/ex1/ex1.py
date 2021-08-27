import sys
sys.stdin = open('input.txt')

# 전위 순회
def pre_order(n):
    if n:   # 유효한 정점이면
        print(n, end=" ")
        pre_order(left[n])    # n의 왼쪽자식으로 이동
        pre_order(right[n])


# 중위 순회
def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=" ")
        in_order(right[n])


# 후위 순회
def post_order(n):
    if n:
        in_order(left[n])
        in_order(right[n])
        print(n, end=" ")

# 후위 순회

V = int(input())
edge = list(map(int, input().split()))
E = V - 1               # V개의 정점이 있는 트리의 간선 수
left = [0] * (V+1)      # 부모를 인덱스로 자식번호 저장
right = [0] * (V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽자식이 없으면
        left[p] = c
    else:               # 왼쪽자식이 있으면 오른쪽 자식으로 저장
        right[p] = c

pre_order(1)
print()
in_order(1)
print()
post_order(1)