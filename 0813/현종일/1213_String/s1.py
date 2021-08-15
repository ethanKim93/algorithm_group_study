import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for tc in range(1, 11):
    N = int(input())
    search = input()
    sen = input()

    result = 0
    for i in range(len(sen)):
        if sen[i] == search[0]:
            cnt = 1
            if len(sen) - len(search) >= i:
                for j in range(1, len(search)):
                    if sen[i+j] != search[j]:
                        break
                    cnt += 1
                if cnt == len(search):
                    result += 1
    print('#{} {}'.format(N, result))

