import sys
sys.stdin = open("input.txt")

num = 100


def check_pal(text):
    if text == text[::-1]:
        return True
    return False


for tc in range(1,11):
    T = int(input())
    row_matrix = [input() for _ in range(num)]
    col_matrix = list(zip(*row_matrix))
    max_interval = 1

    for temp_interval in range(num, 1, -1):
        if max_interval > temp_interval:
            break
        for idx in range(num - temp_interval + 1):
            for i in range(num):
                if check_pal(row_matrix[i][idx : idx + temp_interval]) or check_pal(col_matrix[i][idx : idx + temp_interval]):
                    max_interval = temp_interval
                    break

    print("#{} {}".format(tc, max_interval))