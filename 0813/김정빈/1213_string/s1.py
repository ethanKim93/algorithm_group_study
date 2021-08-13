import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for tc in range(1, 11):
    T = int(input())
    p = input() #찾을 패턴
    text = input() #전체 텍스트

    M = len(p) #찾을 패턴의 길이
    N = len(text) #전체 텍스트 길이

    cnt = 0

    i = 0
    j = 0

    while j < M and i < N:
        if text[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

        if j == M:
            cnt += 1
            j = 0

    print('#{} {}'.format(tc, cnt))