import sys
sys.stdin = open('test_input.txt', encoding='UTF-8')

for tc in range(1, 11):
    ta = input()
    word = input()
    sentence = input()

    word_len = len(word)
    sentence_len = len(sentence)
    j = 0  # word index
    i = 0  # sentence index
    cnt = 0
    total_cnt = 0

    while i < sentence_len:
        if sentence[i] != word[j]:  # 문장에서 단어 알파벳을 못 찾을 경우
            cnt = 0
            i -= j
            j = -1
        else:  # 문장에서 단어 알파벳을 찾는 경우
            cnt += 1
        i += 1
        j += 1
        if cnt == len(word):  # 알파벳 개수와 단어 길이가 같으면 total 1 추가
            total_cnt +=1
            j = 0
    print('#{} {}'.format(tc, total_cnt))






