# 지빈님, 진석님

import sys
sys.stdin = open('sample_input.txt', 'r')


def push(S, x, top):
    top += 1
    S[top] = x


def pop(S, top):
    top -= 1
    return S[top+1]


def dfs():
    global searchstart
    start = searchstart[0]
    # dfs 할 때 사용 stack
    stack = [None] * 1000000
    top = -1
    push(stack, start, top)
    while searchstart:
        # 방문한 노드는 리스트에서 없앤다
        v = pop(stack, top)
        for i in adjli[v]:
            push()



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    team = list(map(int, input().split()))
    adjli = [[] for _ in range(N+1)]
    # 인접리스트 만들기 / 무향그래프
    for i in range(M):
        adjli[team[2*i]].append(team[2*i+1])
        adjli[team[2*i+1]].append(team[2*i])
    print(adjli)
    # 맨 앞에 있는거 꺼내서 dfs 하기
    searchstart = [j for j in range(1, N+1)]
    visited

