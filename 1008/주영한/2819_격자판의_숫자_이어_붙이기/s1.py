T = int(input())

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def find(row, col, cnt, temp):
    if cnt == 7:
        diffent_set.add("".join(map(str, temp)))
        return

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            temp.append(maps[new_row][new_col])
            find(new_row, new_col, cnt + 1, temp)
            temp.pop()
    return

for tc in range(1, T + 1):
    maps = [list(map(int, input().split())) for _ in range(4)]
    diffent_set = set()
    for row in range(4):
        for col in range(4):
            find(row, col, 0, [])
    print("#{} {}".format(tc, len(diffent_set)))