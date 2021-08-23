import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1,1+T):
    words = [list(map(str,input())) for _ in range(5)]
    print(words)

    lis = []
    max_len = 0

    for word in words:
        lis.append(len(word))
        if len(word) > max_len:
            max_len = len(word)


    res = ''
    for q in range(max_len):
        for w in range(5):
            if lis[w] > q:
                res += words[w][q]

    print('#{} {}'.format(tc,res))