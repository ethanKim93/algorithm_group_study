import sys
sys.stdin = open('sample_input.txt')


def search_word(word, sentence):
    word_len = len(word)
    sentence_len = len(sentence)
    j = 0  # word index
    i = 0  # sentence index
    while i < sentence_len and j < word_len:
        if sentence[i] != word[j]:  # 문장에서 단어 알파벳을 못 찾을 경우
            i -= j
            j = -1
        i += 1
        j += 1
    if j == word_len:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    word = input()
    sentence = input()

    print('#{} {}'.format(tc, search_word(word, sentence)))