import sys
sys.stdin = open("sample_input.txt")

def search_min(row):
    global min_sum, my_sum

    if my_sum > min_sum:
        return

    if row == N and my_sum < min_sum:
        min_sum = my_sum
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            my_sum += arr[row][col]
            search_min(row + 1)
            my_sum -= arr[row][col]
            visited[col] = False

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N
    my_sum = 0
    visited = [False] * N

    search_min(0)
    print('#{} {}'.format(tc, min_sum))