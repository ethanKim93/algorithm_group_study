import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for tc in range(1, 11):
    N = int(input())
    text = input()
    texts = input()

    cnt = 0
    for i in range(0, len(texts)-1):
        if texts[i] == text[0]:
            if texts[i:i+len(text)] == text:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
