import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc, N = map(int, input().split())
    pair = list(map(int, input().split()))

    # 가이드처럼 각 정점에서 도착하는 정점의 번호를 저장하는 list 2개 만들기
    arr1 = [0] * 100
    arr2 = [0] * 100
    j = 1
    for i in range(0, N*2-1, 2):
        if j % 2:
            arr1[pair[i]] = pair[i+1]
        else:
            arr2[pair[i]] = pair[i+1]
        j += 1

    visited = [0] * 100  # 방문 여부 체크
    stack = [0]  # 지금까지 지나왔던 노드 저장
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            for v in [arr1[vertex], arr2[vertex]]:
                if v != 0:
                    if not visited[v]:
                        stack.append(v)

    result = 1 if visited[99] else 0
    print('#{} {}'.format(tc, result))