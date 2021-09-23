"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

"""

#전위순회
def pre_order(n):
    if n: # 유효한 정점이면 (자식이 있으면)
        print(n, end=" ")
        pre_order(left[n])
        pre_order(right[n])
#중위순회
def in_order(n):
    if n:

        in_order(left[n])
        print(n, end=" ")
        in_order(right[n])

#후위순회
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end=" ")


V= int(input()) # 트리의 간선수

treelink=list(map(int,input().split()))
S=treelink[0]
left=[0] *(V+1)
right=[0] *(V+1)
stack=[]
for i in range(V-1):
    parent,child=treelink[2*i],treelink[2*i+1]

    if not stack:
        stack.append(parent)
        left[parent]=child
    elif stack[-1]!=parent:
        stack.pop()
        stack.append(parent)
        left[parent]=child
    elif stack[-1]==parent:
        stack.pop()
        stack.append(parent)
        right[parent]=child

print(left)
print(right)
pre_order(1)
print()
in_order(1)
print()
post_order(1)