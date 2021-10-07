N = int(input())
adj = [[] for _ in range(N)]
input_queue = list(map(int, input().split()))
for i in range(N):
    adj[input_queue[2 * i]].append(input_queue[2 * i + 1])

def preorder(node):

    print(node, end=" ")
    if len(adj) > node:
        if len(adj[node]) > 0:
            preorder(adj[node][0])
        if len(adj[node]) > 1:
            preorder(adj[node][1])
    return

def inorder(node):

    if len(adj) > node:
        if len(adj[node]) > 0:
            inorder(adj[node][0])

    print(node, end=" ")

    if len(adj) > node:
        if len(adj[node]) > 1:
            inorder(adj[node][1])
    return

def postorder(node):
    if len(adj) > node:
        if len(adj[node]) > 0:
            postorder(adj[node][0])

        if len(adj[node]) > 1:
            postorder(adj[node][1])
    print(node, end=" ")
    return

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()