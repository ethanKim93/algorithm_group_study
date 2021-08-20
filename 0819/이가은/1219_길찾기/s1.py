import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test, N = map(int, input().split())
    li = list(map(int, input().split()))

    a = []
    b = []

    for i in range(0, 2*N, 2):
        a.append(li[i])
        b.append(li[i+1])

    graph = [[0] * 100 for _ in range(100)]

    for j in range(len(a)):
        graph[a[j]][b[j]] = 1

    result = 0
    s = 0
    e = 99
    stack = [s]
    visited = [s]

    while stack:
        for i in range(100):
            if graph[stack[-1]][i] == 1:
                graph[stack[-1]][i] = 0
                stack.append(i)
                visited.append(i)

                if i == e:
                    result = 1
                    break

                break
        else:
            stack.pop(-1)
        if result:
            break

    print('#{} {}'.format(test, result))