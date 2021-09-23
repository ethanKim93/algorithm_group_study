import sys
sys.stdin = open('sample_input.txt')

# def postorder(t):
#     # global tree
#     if t <= N and not tree[t]:
#         postorder(2*t)
#         postorder(2*t + 1)
#         if 2*t + 1 <= N:
#             tree[t] = tree[2*t] + tree[2*t + 1]
#         else:
#             tree[t] = tree[2*t]

# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#     for _ in range(M):
#         a, b = map(int, input().split())
#         tree[a] = b
#     postorder(1)
#     print('#{} {}'.format(tc, tree[L]))

def postorder(t):
    if t <= N:
        postorder(2*t)
        postorder(2*t + 1)
        tree[t//2] += tree[t]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    postorder(1)
    print('#{} {}'.format(tc, tree[L]))