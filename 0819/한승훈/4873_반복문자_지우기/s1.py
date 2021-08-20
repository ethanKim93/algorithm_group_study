import sys
sys.stdin = open('sample_input.txt')

T = int(input())


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



for tc in range(1, T+1):
    words = list(input())
    word = []
    dupl(words)
    print('#{} {}'.format(tc, len(word)))


