import sys
sys.stdin = open('input.txt')


def dfs():
    visited = [0] * 100
    stack = []
    i = 0
    visited[i] = 1
    while i != -1:
        for w in range(100):
            if not visited[arr1[i]]:
                stack.append(i)
                i = arr1[i]
                visited[i] = 1
                if i == 99:
                    return 1
                break
            elif not visited[arr2[i]]:
                stack.append(i)
                i = arr2[i]
                visited[i] = 1
                if i == 99:
                    return 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = -1
    return 0


for tc in range(1, 11):
    T, E = map(int, input().split())
    routes = list(map(int, input().split()))
    arr1 = [0] * 100
    arr2 = [0] * 100
    idx = 0
    for i in range(E * 2):
        if not i % 2:
            idx = routes[i]
        else:
            if not arr1[idx]:
                arr1[idx] = routes[i]
            else:
                arr2[idx] = routes[i]

    print('#{} {}'.format(tc, dfs()))