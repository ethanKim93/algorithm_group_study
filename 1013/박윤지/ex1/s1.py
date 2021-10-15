# DFS 구현하기
# 재귀는 많이 해봐서, 스택 사용한 반복구조로 하기로

# 입력값
# 7
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

import sys
sys.stdin = open('input.txt')

N = int(input())
edge = list(map(int, input().split()))  # 무방향
adj = [[] for _ in range(N+1)]
for i in range(len(edge)//2):
    adj[edge[2*i]].append(edge[2*i+1])
    adj[edge[2*i+1]].append(edge[2*i])
# print(adj)
visited = [0 for _ in range(N+1)]
ans = []

# 스택
STACK_SIZE = N+1  # DFS 돌면서 정점이 중복으로 들어갈 수가 없어서 N+1을 한듯
stack = [0] * STACK_SIZE
top = -1

def push(s, x):
    global top
    top += 1
    s[top] = x


def pop(s):
    global top
    top -= 1
    return s[top+1]


def isEmpty(s):
    if top == -1:
        return True
    else:
        return False

def peek(s):
    global top
    return s[top]


def dfs(V):  # V: 시작 정점
    global stack
    push(stack, V)
    visited[V] = 1
    while not isEmpty(stack):
        u = pop(stack)
        ans.append(u)
        for j in adj[u]:
            if not visited[j]:
                push(stack, j)
                visited[j] = 1

dfs(1)
print(*ans)
