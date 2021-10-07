"""
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def goto(mode, node=1):
    if mode == "front":
        print(node, end=" ")

    try:
        goto(mode, tree[node][0])
    except IndexError:
        pass

    if mode == "middle":
        print(node, end=" ")

    try:
        goto(mode, tree[node][1])
    except IndexError:
        pass

    if mode == "last":
        print(node, end=" ")


V = int(input())
nums = list(map(int, input().split()))

tree = [[] for _ in range(V + 1)]

for i in range(0, V):
    tree[nums[i*2]].append(nums[i*2+1])

goto("front")
print()
goto("middle")
print()
goto("last")
