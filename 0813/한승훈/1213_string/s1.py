import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for _ in range(1, 11):
    tc = int(input())
    find_num = input()
    words = input()
    N = len(find_num)
    i = 0
    cnt = 0
    while i+N <= len(words):
        if find_num == words[i:i+N]:
            cnt += 1
            i += N
        else:
            i += 1

    print('#{} {}'.format(tc, cnt))
