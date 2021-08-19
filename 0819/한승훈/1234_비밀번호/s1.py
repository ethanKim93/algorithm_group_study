import sys
sys.stdin = open('input.txt')


def dupl(words):
    global word
    for idx in range(len(words)-1):
        if words[idx] == words[idx+1]:
            words.pop(idx+1)
            words.pop(idx)
            word = words
            return dupl(word)
    else:
        return word



for tc in range(1, 11):
    N, p = map(str, input().split())
    words = list(p)
    word = []
    dupl(words)
    print('#{} {}'.format(tc, ''.join(word)))