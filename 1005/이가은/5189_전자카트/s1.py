import sys
sys.stdin = open('sample_input.txt')

def office(idx, total):
    global value

    if 0 not in visited:
        if value > total:
        return
    elif value < total:
        return

    for i in range(N):
        if i == idx or visited[i]:
            continue
        elif i == 0 and 0 in visited[1:]:
            continue
        visited[i] = 1
        office(i, total + arr[idx][i])
        visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    value = 1000000
    office(0, 0)

    print('#{} {}'.format(tc, value))