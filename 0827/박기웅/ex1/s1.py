# 전위 순회
def pre_order(v):
    if v:
        print(v, end=" ")
        pre_order(left[v])
        pre_order(right[v])

# 중위 순회
def in_order(v):
    if v:
        in_order(left[v])
        print(v, end=" ")
        in_order(right[v])
# 후위 순회
def post_order(v):
    if v:
        post_order(left[v])
        post_order(right[v])
        print(v, end=" ")

V = 13
edge = list(map(int, "1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13".split()))
E = V - 1 # 트리 구조의 노드 당 간선 수

left = [0]*(V+1)
right = [0]*(V+1)

# 부모 노드 - 자식 노드(왼, 오) 할당
for i in range(E):
    p, c = edge[2*i], edge[2*i+1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
print("Pre-order: ", end= " ")
pre_order(1)
print()

print("In-order: ", end= " ")
in_order(1)
print()

print("Post-order: ", end= " ")
post_order(1)
print()





