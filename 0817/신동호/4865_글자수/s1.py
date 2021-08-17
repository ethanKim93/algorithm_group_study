import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    letters = set(str1)
    book = {}
    for word in str2:
        if (word in letters) and (word in book):
            book[word] += 1
        elif word in letters:
            book[word] = 1
    result = 0
    for value in book.values():
        if result < value:
            result = value

    print('#{} {}'.format(tc, result))