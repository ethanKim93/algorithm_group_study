import sys
sys.stdin = open('input.txt')

def check(words):
    if words==words[::-1]:
        return True
    else:
        return False
for _ in range(10):
    test_case = int(input())
    arr = [list(input()) for _ in range(100)]
    max_len = 0
    for i in range(100):
        for j in range(100):
            for len_word in range(1, 101-j):
                row_word = ''
                col_word = ''
                for k in range(len_word):
                    row_word += arr[i][j+k]
                    col_word += arr[j+k][i]
                if check(row_word):
                    if len_word > max_len:
                        max_len = len_word
                if check(col_word):
                    if len_word > max_len:
                        max_len = len_word
    print('#{} {}'.format(test_case,max_len))
