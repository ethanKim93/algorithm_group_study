import sys
sys.stdin = open("input.txt")

def inorder_traversal(left_child, right_child, parent, data):
    if parent:
        inorder_traversal(left_child, right_child, left_child[parent], data)
        print(data[parent], end="")
        inorder_traversal(left_child, right_child, right_child[parent], data)
    return


for tc in range(1, 11):
    N = int(input())

    data = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(1, N + 1):
        inform = input().split()
        data[int(inform[0])] = inform[1]
        L = len(inform)
        if L == 4:
            left[int(inform[0])] = int(inform[2])
            right[int(inform[0])] = int(inform[3])
        if L == 3:
            left[int(inform[0])] = int(inform[2])

    print("#{}".format(tc), end=" ")
    inorder_traversal(left, right, 1, data)
    print()