import sys
sys.stdin = open("input.txt")

def transpose(matrix):
    L = len(matrix)
    for row in range(L):
        for col in range(row, L):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

for tc in range(1, 11):
    dummy = input()
    magentic_field = [list(map(int, input().split())) for _ in range(100)]
    transpose(magentic_field)

    result = 0

    # magentic_field = [list(filter(lambda x : x, col_field)) for col_field in magentic_field]

    # for col_field in magentic_field:
    #     while col_field[0] != 1:
    #         col_field.pop(0)
    #     while col_field[-1] != 2:
    #         col_field.pop()
    #     print(col_field)
    #     for num in col_field:
    #         result += 1
    for col_field in magentic_field:
        magetic_buffer = 0
        for row in col_field:
            if row:
                if magetic_buffer == 1 and row == 2:
                    result += 1
                magetic_buffer = row

    print("#{} {}".format(tc, result))