def color(index, c, N):
    result = 0
    for i in range(len(matrix[index])):
        if matrix[index][i] != c:
            result += 1
    if index == N:
        return result
    if c == 'W':
        if index == N - 1:
            result += color(index + 1, 'B', N)
        else:
            result += min(color(index + 1, 'W', N), (index + 1, 'B', N))
    elif c == 'B':
        result += min(color(index + 1, 'B', N), color(index + 1, 'R', N))
    else:
        result += color(index + 1, 'R', N)
    return result
T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    cnt = 0
    for i in range(M):
        if matrix[0][i] != 'W':
            cnt += 1
        if matrix[N-1][i] != 'R':
            cnt += 1
    cnt += min(color(1, 'W', N - 2), color(1, 'B', N - 2))

    print("#{} {}".format(tc, cnt))