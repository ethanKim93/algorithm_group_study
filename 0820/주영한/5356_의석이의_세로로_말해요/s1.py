import sys
sys.stdin = open("sample_input.txt")

def extend(length, list_inputs):
    result = [-1] * length
    for idx, list_input in enumerate(list_inputs):
        result[idx] = list_input
    return result


def speak_col(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = []
    for c in range(col):
        for r in range(row):
            if matrix[r][c] != -1:
                result.append(matrix[r][c])
    return "".join(result)

T = int(input())
for tc in range(1, T + 1):
    matrix = [input() for _ in range(5)]
    max_col = 0
    for row in range(5):
        if len(matrix[row]) > max_col:
            max_col = len(matrix[row])
    matrix = list(map(lambda x : extend(max_col, x), matrix))
    print("#{} {}".format(tc, speak_col(matrix)))