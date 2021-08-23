import sys
sys.stdin = open("sample_input.txt")
'''
가로 단어중 최대 길이를 구하고
이 최대 길이를 이용하여 이보다 작은 길이의 문자는 공문자로 concatenate
이후 2차원 배열을 하나씩 붙여서 단어를 만듦
'''
for tc in range(1, int(input())+1):
    words = [list(input()) for _ in range(5)]

    maxlen = 0
    for word in words:
        if maxlen < len(word):
            maxlen = len(word)

    for word in words:
        if len(word) < maxlen:
            word += ['']*(maxlen-len(word))

    ans = ''
    for listx in [list(x) for x in zip(*words)]:
        for s in listx:
            ans += s
    print('#{} {}'.format(tc, ans))