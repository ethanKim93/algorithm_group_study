import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    max_cnt = 0
    for letter1 in str1:
        for letter2 in str2:
            if letter1 == letter2:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
    print('#{} {}'.format(tc, max_cnt))