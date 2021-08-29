import sys
sys.stdin = open("input.txt")


def preorder_traversal(left_child, right_child, parent):
    if parent:
        print(parent, end=" ")
        preorder_traversal(left_child, right_child, left_child[parent])
        preorder_traversal(left_child, right_child, right_child[parent])
    return


def inorder_traversal(left_child, right_child, parent):
    if parent:
        inorder_traversal(left_child, right_child, left_child[parent])
        print(parent, end=" ")
        inorder_traversal(left_child, right_child, right_child[parent])
    return


def postorder_traversal(left_child, right_child, parent):
    if parent:
        postorder_traversal(left_child, right_child, left_child[parent])
        postorder_traversal(left_child, right_child, right_child[parent])
        print(parent, end=" ")
    return



node_num = int(input())
left_child = [0] * (node_num + 1)
right_child = [0] * (node_num + 1)
connections = list(map(int, input().split()))
for idx in range(0, len(connections), 2):
    temp_parent = connections[idx]
    temp_child = connections[idx + 1]
    if left_child[temp_parent]:
        right_child[temp_parent] = temp_child
    else:
        left_child[temp_parent] = temp_child

print("preorder_traversal")
preorder_traversal(left_child, right_child, 1)
print()
print("inorder_traversal")
inorder_traversal(left_child, right_child, 1)
print()
print("preorder postorder_traversal")
postorder_traversal(left_child, right_child, 1)