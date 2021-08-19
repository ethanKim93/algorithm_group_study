import sys

sys.stdin = open("input.txt")

for a in range(0, 10):
    tc, n = map(int, input().split())
    num_list = list(map(int, input().split()))

    dic = {x: [] for x in range(100)}
    for i in range(0, n * 2, 2):
        my_key = num_list[i]
        my_val = num_list[i + 1]
        dic[my_key].append(my_val)

    stack = [0]
    visited = stack * 100
    visited[0] = 1
    answer = 0

    while stack:
        c = stack.pop()
        for j in dic[c]:
            if j == 99:
                answer = 1
                break
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1

    print('#{} {}'.format(tc + 1, answer))
