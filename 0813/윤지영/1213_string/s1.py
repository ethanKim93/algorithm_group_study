import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

T = 10

for _ in range(T):
    tc = int(input())
    target = input()
    l = len(target)
    sen = input()
    cnt = 0
    for i in range(len(sen)):
        if target in sen[i:i+l]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))