import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T, E = map(int, input().split())
    a1 = list(map(int,input().split()))
    route = [[] * 100 for _ in range(100)]

    for i in range(0, E*2, 2):
        start = a1[i]
        move = a1[i+1]
        route[start].append(move)

    visited = [0] * 100
    stack = [0]
    ans = 0
    while stack:
        a = stack.pop()
        if not visited[a]:
            visited[a] += 1
            for w in route[a]:
                if not visited[w]:
                    stack.append(w)
    print('#{} {}'.format(tc, visited[99]))