import sys
sys.stdin = open('sample_input.txt')

T = int(input())
N = 5

for tc in range(1, T+1):
    matrix = []
    max_len = 0
    for _ in range(N):
        word = list(input())
        if len(word) > max_len:
            max_len = len(word)
        matrix.append(word)
    result = ''
    for i in range(max_len):
        for j in range(5):
            try:
                result += matrix[j][i]
            except:
                pass
    print('#{} {}'.format(tc, result))