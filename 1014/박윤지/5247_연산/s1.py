# 런타임에러
# 채은님, 명수님

import sys
sys.stdin = open('sample_input.txt')

# from collections import deque

# def bfs(num):
#     global cnt
#     queue = deque([(num, 0)])
#     while queue:
#         q = queue.popleft()
#         v = q[0]
#         vc = q[1]
#         for i in range(4):
#             if i == 0:
#                 if v+1 == M:
#                     return vc+1
#                 if 1 <= v+1 <= 1000000:
#                     queue.append((v+1, vc+1))
#             elif i == 1:
#                 if v-1 == M:
#                     return vc+1
#                 if 1 <= v-1 <= 1000000:
#                     queue.append((v-1, vc+1))
#             elif i == 2:
#                 if v*2 == M:
#                     return vc+1
#                 if 1 <= v*2 <= 1000000:
#                     queue.append((v*2, vc+1))
#             elif i == 3:
#                 if v-10 == M:
#                     return vc+1
#                 if 1 <= v-10 <= 1000000:
#                     queue.append((v-10, vc+1))

def enQueue(queue, x):
    global rear
    rear += 1
    queue[rear] = x


def deQueue(queue):
    global front
    front += 1
    return queue[front]


def bfs(num):
    enQueue(queue, (num, 0))
    while queue:
        q = deQueue(queue)
        v = q[0]
        vc = q[1]
        v1, v2, v3, v4 = v+1, v-1, v*2, v-10

        if M in [v1, v2, v3, v4]:
            return vc+1
        if 1 <= v1 <= 1000000:
            enQueue(queue, (v1, vc+1))
        if 1 <= v2 <= 1000000:
            enQueue(queue, (v2, vc+1))
        if 1 <= v3 <= 1000000:
            enQueue(queue, (v3, vc+1))
        if 1 <= v4 <= 1000000:
            enQueue(queue, (v4, vc+1))


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # BFS
    queue = [None] * 1000000
    front, rear = -1, -1

    print('#{} {}'.format(tc, bfs(N)))