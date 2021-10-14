import sys
from collections import deque
sys.stdin = open('input.txt')
# 어떻게 접근해야할지 구글링하다가..
# 람다로 정리 해봤습니다.

def match(x,value):
    result = {
        1: lambda x: x + 1,
        2: lambda x: x - 1,
        3: lambda x: x * 2,
        4: lambda x: x - 10,
    }[value](x)
    return result

def BFS():
    global total
    while queue:
        n,cnt=queue.popleft()
        if n == M:
            total=cnt
            return
        for i in range(1, 5):
            cac=match(n,i)
            if  0 < cac <= 1000000 and cac_visited[cac] == 0:
                queue.append((cac,cnt+1))
                cac_visited[cac]=1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    cac_visited = [0] * 1000001
    total=0
    queue = deque()
    queue.append((N, 0))
    BFS()
    print('#{} {}'.format(tc,total))



