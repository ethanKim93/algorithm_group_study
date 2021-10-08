import sys
sys.stdin = open('sample_input.txt')

yx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(T):
    arr = [input().split() for _ in range(4)]
    result = set()
    empty = []
    for i in range(4):
        for j in range(4):
            empty.append((i, j, 0, arr[i][j]))
            while empty:
                y, x, count, ans = empty.pop()
                if count >= 6:
                    result.add(ans)
                    continue
                for d_y, d_x, in yx:
                    dy = d_y + y
                    dx = d_x + x
                    if 0 <= dy < 4 and 0 <= dx < 4:
                        empty.append((dy, dx, count + 1, ans + arr[dy][dx]))

    print('#{} {}'.format(tc + 1, len(result)))