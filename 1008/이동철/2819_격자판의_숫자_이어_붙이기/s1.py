import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(idx, x, y, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    num += arr[x][y]
    if idx == 6:
        # 6번 이동한 결과 값 result 배열에 추가
        result.append(num)
        return
    for i in range(4):
        if 0 <= x + dx[i] < 4 and 0 <= y + dy[i] < 4:
            # 벽 체크
            dfs(idx + 1, x + dx[i], y + dy[i], num)


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for x in range(4):
        for y in range(4):
            dfs(0, x, y, "")

    answer = set(result)
    print('#{} {}'.format(tc, len(answer)))