import sys
sys.stdin = open('sample_input.txt')


def search_palindrome(N, M, word_list):
    for i in range(N):
        for j in range(N-M+1):
            row_word = col_word = ''
            for k in range(M):
                row_word += word_list[i][j+k]
                col_word += word_list[j+k][i]
            if row_word == row_word[::-1]:
                return row_word
            elif col_word == col_word[::-1]:
                return col_word
    return 'no answer'

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_list = [list(input()) for _ in range(N)]

    print('#{} {}'.format(tc, search_palindrome(N, M, word_list)))


