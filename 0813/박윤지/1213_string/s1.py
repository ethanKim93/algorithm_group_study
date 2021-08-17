import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF-8')

T = 10
for tc in range(1, T+1):
    testcase = int(input())
    target = input()
    sent = input()
    result = 0
    for i in range(len(sent) - len(target) + 1):
        for j in range(len(target)):
            if sent[i+j] != target[j]:
                break
        else:
            result += 1
    print('#{} {}'.format(tc, result))