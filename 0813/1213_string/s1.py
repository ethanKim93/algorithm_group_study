import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for i in range(10):
    t = int(input())
    patt = input()
    sentence = input()

    cnt = 0
    for i in range(len(senten) - len(patt) + 1):
        if senten[i:i + len(patt)] == patt:
            cnt += 1

    print('#{} {}'.format(t, cnt))
