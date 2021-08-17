import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for char1 in str1:
        temp = 0
        for char2 in str2:
            if char2 == char1:
                temp += 1
        if max_cnt < temp:
            max_cnt = temp
    print('#{} {}'.format(tc, max_cnt))