import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    max_length = 0
    words = []
    for _ in range(5):
        i = input()
        words.append(i)
        if max_length < len(i):
            max_length = len(i)

    result = ''
    for idx in range(max_length):
        for word in words:
            if len(word)-1 >= idx:
               result += word[idx]

    print('#{} {}'.format(tc, result))



