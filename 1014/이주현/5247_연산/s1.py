import sys
sys.stdin = open('sample_input.txt')

from collections import deque

MAX_VALUE = 1000000
MIN_VALUE = 1

def BFS():
    global result
    while queue: #큐가 비어있지 않으면
        front, check = queue.popleft()
        if front == M:
            result = check
            return #함수 종료
        for i in range(4):
            if i == 0:
                if MIN_VALUE <= front + 1 <= MAX_VALUE and visited[front+1] == 0:
                    queue.append((front+1, check+1))
                    visited[front+1] = 1
            elif i == 1:
                if MIN_VALUE <= front - 1 <= MAX_VALUE and visited[front-1] == 0:
                    queue.append((front-1, check+1))
                    visited[front - 1] = 1
            elif i == 2:
                if MIN_VALUE <= front * 2 <= MAX_VALUE and visited[front*2] == 0:
                    queue.append((front*2, check+1))
                    visited[front * 2] = 1
            elif i == 3:
                if MIN_VALUE <= front - 10 <= MAX_VALUE and visited[front-10] == 0:
                    queue.append((front-10, check+1))
                    visited[front - 10] = 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    visited = [0] * (MAX_VALUE + 1)
    queue = deque()
    queue.append((N, 0))
    BFS()

    print("#{} {}".format(tc, result))