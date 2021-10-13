import sys
sys.stdin = open("input.txt")

T = int(input())
delta_col = [0, 0, -1, 1]
delta_row = [-1, 1, 0, 0]

for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    numbers = [0] * N**2
    numbers.append(0)
    for row in range(N):
        for col in range(N):
            for i in range(4):
                tmp_row = row + delta_row[i]
                tmp_col = col + delta_col[i]
                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if matrix[row][col] + 1 == matrix[tmp_row][tmp_col]:
                        numbers[matrix[row][col]] = 1

    i = len(numbers) - 1
    result = [0, 0]
    while i > 0:
        count = 0
        if numbers[i] == 1:
            while numbers[i] == 1:
                count += 1
                i -= 1
            if result[1] <= count:
                result[0] = i + 1
                result[1] = count
        else:
            i -= 1

    print("#{} {} {}".format(tc, result[0], result[1] + 1))
