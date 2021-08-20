import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, p = map(str, input().split())
    words = list(p)
    word = []
    for idx in range(len(words)):
        if not word:
            word.append(words[idx])
        elif words[idx] == word[-1]:
            word.pop(-1)
        else:
            word.append(words[idx])

    print('#{} {}'.format(tc, ''.join(word)))
