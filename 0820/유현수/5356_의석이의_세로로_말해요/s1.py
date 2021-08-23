import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    texts = []
    for _ in range(5):
        text = list(input())
        if len(text) < 15:
            n = 15 - len(text)
            for i in range(n):
                text.append(-1)
        texts.append(text)

    print('#{}'.format(tc), end=' ')
    for i in range(15):
        for j in range(5):
            if texts[j][i] == -1:
                pass
            else:
                print(texts[j][i], end='')
    print()
