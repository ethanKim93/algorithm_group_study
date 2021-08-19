import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    table = [1, 3]  # 1, 3, 5, 11, 21, 43, ... 등차수열을 위해 초기값 입력
    for i in range(2, N // 10 + 1):
        table.append(table[i - 1] + 2 * table[i - 2])
    print('#{} {}'.format(tc, table[N // 10 - 1]))
