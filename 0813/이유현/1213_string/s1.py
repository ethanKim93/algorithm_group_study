import sys
sys.stdin = open('test_input.txt', encoding='UTF-8')

for i in range(1, 11):
    tc = int(input())

    find = input()
    sent = input()

    flen = len(find)
    slen = len(sent)
    cnt = 0
    for i in range(slen - flen + 1):
        letter = 0
        for j in range(flen):
            if sent[i+j] == find[j]:
                letter += 1
        if letter == flen:
            cnt += 1
    print('#{} {}'.format(tc, cnt))

    # cnt = sent.count(find)
    # print('#{} {}'.format(tc, cnt))