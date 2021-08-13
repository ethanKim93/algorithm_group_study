import sys
sys.stdin = open('test_input.txt', encoding='UTF-8')

for i in range(1, 11):
    tc = int(input())

    find = input()
    sent = input()
    cnt = sent.count(find)
    print('#{} {}'.format(tc, cnt))