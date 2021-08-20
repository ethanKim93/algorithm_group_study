import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def test(text):
    i = 1
    while i < len(text):
        if text[i] == text[i-1]:
            text = text[0:i-1] + text[i+1:]
            return test(text)
        else:
            i += 1
    return text


for tc in range(1, T+1):
    text = list(input())
    print('#{} {}'.format(tc, len(test(text))))